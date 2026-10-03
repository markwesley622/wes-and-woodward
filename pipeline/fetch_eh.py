#!/usr/bin/env python3
"""Nightly Evolving-Hockey pull: the current season's skater GAR, xGAR and RAPM (EV + PK) tables,
merged into the all-seasons CSVs the player builder reads (research/rasmussen/raw/eh/).

Runs headless with the session saved by pipeline/eh_login.py (~/.config/wesandwoodward/eh_state.json).
The Shiny apps take their inputs from the URL (?_inputs_&gar_sk_season="20262027"...), so each table
is one page load + one click on its Download link. If EH has not published the season yet (it is
missing from the season selector), the script says so and exits 0; the rest of the nightly job
carries on with last season's files.

Usage: python3 pipeline/fetch_eh.py [--season 20262027]
"""
import csv, io, json, pathlib, sys, urllib.parse
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

ROOT = pathlib.Path(__file__).resolve().parents[1]
EH = ROOT / "research" / "rasmussen" / "raw" / "eh"
STATE = pathlib.Path.home() / ".config" / "wesandwoodward" / "eh_state.json"
CFG = json.loads((ROOT / "pipeline" / "config.json").read_text())
SEASON = sys.argv[sys.argv.index("--season") + 1] if "--season" in sys.argv else CFG["nhl_season"]
EH_SEASON = f"{SEASON[2:4]}-{SEASON[6:8]}"

# table -> (page, input prefix, extra inputs, download link id, target file)
TABLES = {
    "gar": ("stats/skater_gar/", "gar_sk", {"base": "Replacement", "type": "Totals", "col": "Basic", "toi_all": "1", "toi_ev": "0", "toi_pp": "0", "toi_sh": "0"}, "gar_sk_download", "gar_all_seasons.csv"),
    "xgar": ("stats/skater_xgar/", "xgar_sk", {"base": "Replacement", "type": "Totals", "col": "Basic", "toi_all": "1", "toi_ev": "0", "toi_pp": "0", "toi_sh": "0"}, "xgar_sk_download", "xgar_all_seasons.csv"),
    "rapm_ev": ("stats/skater_rapm/", "rapm_sk", {"table": "Single-Season", "str": "EV", "type": "Rates", "toi": "1"}, "rapm_sk_download", "rapm_ev_rates_all_seasons.csv"),
    "rapm_pk": ("stats/skater_rapm/", "rapm_sk", {"table": "Single-Season", "str": "SH", "type": "Rates", "toi": "1"}, "rapm_sk_download", "rapm_pk_rates_2023-2025.csv"),
}
COMMON = {"team": "All", "pos": "All", "info": "No", "status": "All", "range": "Seasons", "span": "Regular", "group": "Team, Season", "dft_yr": "All", "age1": "17", "age2": "50"}


def page_url(page, prefix, extra):
    inputs = dict(COMMON); inputs.update(extra); inputs["season"] = SEASON
    q = "&".join(f"{prefix}_{k}={urllib.parse.quote(json.dumps(v))}" for k, v in inputs.items()) + f"&{prefix}_players=null"
    return f"https://evolving-hockey.com/{page}?_inputs_&{q}"


def merge(target, text):
    rows = list(csv.DictReader(io.StringIO(text)))
    if not rows: return 0, "empty download"
    seasons = {r.get("Season") for r in rows}
    if seasons != {EH_SEASON}: return 0, f"unexpected seasons in download: {sorted(seasons)}"
    path = EH / target
    old = list(csv.DictReader(path.open())) if path.exists() else []
    header = list(rows[0].keys())
    if old and list(old[0].keys()) != header: return 0, f"column mismatch vs {target}: {header}"
    kept = [r for r in old if r.get("Season") != EH_SEASON]
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=header, quoting=csv.QUOTE_NONNUMERIC); w.writeheader(); w.writerows(kept + rows)
    return len(rows), "ok"


def main():
    if not STATE.exists():
        print("EH: no saved session; run python3 pipeline/eh_login.py once"); return 0
    EH.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(storage_state=str(STATE), accept_downloads=True)
        pg = ctx.new_page()
        for name, (page, prefix, extra, dl_id, target) in TABLES.items():
            pg.goto(page_url(page, prefix, extra), wait_until="domcontentloaded")
            try:
                pg.wait_for_selector(f"#{prefix}_season", timeout=30000)
            except PWTimeout:
                if "login" in pg.url or pg.locator("text=Log In").count():
                    print("EH: session expired; run python3 pipeline/eh_login.py again"); browser.close(); return 0
                print(f"EH {name}: page did not load"); continue
            offered = pg.eval_on_selector(f"#{prefix}_season", "e => [...e.options].map(o => o.value)")
            if SEASON not in offered:
                print(f"EH: {SEASON} not published yet for {name} (latest {offered[0] if offered else '?'})"); continue
            pg.click(f"#{prefix}_submit")
            pg.wait_for_timeout(4000)
            with pg.expect_download(timeout=60000) as dl:
                pg.click(f"#{dl_id}")
            text = pathlib.Path(dl.value.path()).read_text()
            n, note = merge(target, text)
            print(f"EH {name}: {n} rows for {EH_SEASON} -> {target} ({note})")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
