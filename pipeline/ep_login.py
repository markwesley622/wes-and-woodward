#!/usr/bin/env python3
"""One-time EliteProspects login for the unattended prospect pull (same recipe as eh_login.py).

Opens a real Chrome window on eliteprospects.com. Log in there with the premium account (the password
never touches this script), then come back to the terminal and press Enter: the session cookies are
saved to ~/.config/wesandwoodward/ep_state.json, which pipeline/ep_pull.py loads every night.
Re-run this whenever the nightly log says the EP session expired (ep_pull.py exits 2).

Why real Chrome: eliteprospects.com sits behind a Cloudflare challenge that blocks headless Chromium
and even a spoofed headless Chrome (page loads, in-page fetches get 403). A real headed Chrome passes
it at once, so the nightly pull drives one placed off-screen. Keep channel/UA identical here and there.
"""
import pathlib
from playwright.sync_api import sync_playwright

STATE = pathlib.Path.home() / ".config" / "wesandwoodward" / "ep_state.json"
STATE.parent.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False, ignore_default_args=["--enable-automation"])
    ctx = browser.new_context(viewport={"width": 1280, "height": 900})
    page = ctx.new_page()
    page.goto("https://www.eliteprospects.com/login", wait_until="domcontentloaded")
    print("Log in to EliteProspects in the window that opened, then press Enter here.")
    try:
        input()
    except EOFError:
        pass
    ctx.storage_state(path=str(STATE))
    browser.close()
print(f"saved {STATE}")
