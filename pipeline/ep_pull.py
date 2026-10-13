#!/usr/bin/env python3
"""Unattended EliteProspects pull for the prospect system (the nightly replacement for pasting
ep_worker.js into a claude-in-chrome tab).

Drives a real Chrome window placed off-screen (Cloudflare blocks headless Chromium, see ep_login.py)
with the session saved by pipeline/ep_login.py, injects pipeline/ep_worker.js into an EP tab, then runs
the same two queue scripts the manual recipe used:

  1. ep_refresh.py              DET system page + every system player page (force re-pull)
  2. ep_league_pull.py <season> the current season's league tables (skaters by age, goalies by age,
                                goalies all ages). The old tables are set aside first and restored
                                for any key the re-pull did not deliver, so a failed run never leaves
                                a partial season on disk.

ep_receiver.py is started if nothing is listening on 127.0.0.1:8765 and stopped again at the end.
Exit 2 = not logged in (run ep_login.py again), 1 = pull failed; the caller keeps the files on disk.

    python3 pipeline/ep_pull.py            # full pull
    python3 pipeline/ep_pull.py --probe    # open the browser, report login state, exit
"""
import json, pathlib, shutil, socket, subprocess, sys, time
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
PIPE = ROOT / "pipeline"
EP = ROOT / "data" / "raw" / "ep"
STATE = pathlib.Path.home() / ".config" / "wesandwoodward" / "ep_state.json"
CFG = json.loads((PIPE / "config.json").read_text())
YR = int(CFG["nhl_season"][:4])
SEASON = f"{YR}-{YR + 1}"
PORT = 8765
SYSTEM_URL = "https://www.eliteprospects.com/team/60/detroit-red-wings/in-the-system"
REFRESH_TIMEOUT = 40 * 60       # seconds; ~50 player pages
LEAGUE_TIMEOUT = 60 * 60        # ~700 table pages at ~1/s
PROBE = "--probe" in sys.argv


def port_open():
    with socket.socket() as s:
        s.settimeout(1)
        return s.connect_ex(("127.0.0.1", PORT)) == 0


def run(args, timeout):
    print(f"-> {' '.join(args)}", flush=True)
    return subprocess.run([sys.executable, *args], cwd=ROOT, timeout=timeout).returncode == 0


def set_aside(season):
    """Move this season's league tables out of the way so ep_league_pull.py re-pulls them."""
    stash = EP / "league" / f".prev-{season}"
    stash.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in (EP / "league").glob(f"*_{season}_*.json"):
        shutil.move(str(f), stash / f.name); n += 1
    print(f"set aside {n} {season} tables", flush=True)
    return stash


def restore_missing(stash):
    back = 0
    for f in stash.glob("*.json"):
        if not (EP / "league" / f.name).exists():
            shutil.move(str(f), EP / "league" / f.name); back += 1
    shutil.rmtree(stash, ignore_errors=True)
    print(f"restored {back} tables the re-pull did not deliver", flush=True)
    return back


def main():
    if not STATE.exists():
        print(f"no EP session at {STATE}: run pipeline/ep_login.py"); return 2
    receiver = None
    if not port_open() and not PROBE:
        receiver = subprocess.Popen([sys.executable, str(PIPE / "ep_receiver.py")], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(20):
            if port_open(): break
            time.sleep(0.5)
        print("started ep_receiver.py", flush=True)
    rc = 1
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False, ignore_default_args=["--enable-automation"],
                                    args=["--window-position=-3000,-3000", "--window-size=800,600"])
        try:
            ctx = browser.new_context(storage_state=str(STATE), viewport={"width": 1280, "height": 900})
            page = ctx.new_page()
            page.goto(SYSTEM_URL, wait_until="domcontentloaded", timeout=90000)
            t0 = time.time()
            while "moment" in page.title().lower() and time.time() - t0 < 45:      # Cloudflare interstitial
                time.sleep(2)
            if "moment" in page.title().lower():
                print("Cloudflare challenge did not clear"); return 1
            who = page.evaluate("""() => { try { const pp = JSON.parse(document.getElementById('__NEXT_DATA__').textContent).props.pageProps;
                return {loggedIn: !!(pp.gbAttributes && pp.gbAttributes.loggedIn), premium: !!(pp.userData && pp.userData.isPremium)}; } catch (e) { return {error: String(e)}; } }""")
            print("session:", who, flush=True)
            if not who.get("loggedIn"):
                print("EP session expired: run pipeline/ep_login.py"); return 2
            if not who.get("premium"):
                print("EP session is not premium; the age-filtered tables need it"); return 2
            if PROBE:
                return 0
            print(page.evaluate((PIPE / "ep_worker.js").read_text()), flush=True)
            ok = run([str(PIPE / "ep_refresh.py")], REFRESH_TIMEOUT)
            if not ok:
                print("player refresh failed"); return 1
            stash = set_aside(SEASON)
            try:
                ok = (run([str(PIPE / "ep_league_pull.py"), SEASON], LEAGUE_TIMEOUT)
                      and run([str(PIPE / "ep_league_pull.py"), SEASON, "--goalies"], LEAGUE_TIMEOUT // 3)
                      and run([str(PIPE / "ep_league_pull.py"), SEASON, "--goalies", "--all-ages"], LEAGUE_TIMEOUT // 6))
            finally:
                missing = restore_missing(stash)
            print("worker:", page.evaluate("JSON.stringify(window.__ww)"), flush=True)
            rc = 0 if ok and missing == 0 else 1
            # the session cookies roll forward; keep the newest so the login lasts as long as EP allows
            ctx.storage_state(path=str(STATE))
        except subprocess.TimeoutExpired as e:
            print("timed out:", e); rc = 1
        finally:
            browser.close()
            if receiver: receiver.terminate()
    return rc


if __name__ == "__main__":
    sys.exit(main())
