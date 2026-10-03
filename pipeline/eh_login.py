#!/usr/bin/env python3
"""One-time Evolving-Hockey login for the nightly pull.

Opens a real browser window on evolving-hockey.com. Log in there (the password never touches this
script), then come back to the terminal and press Enter: the session cookies are saved to
~/.config/wesandwoodward/eh_state.json, which pipeline/fetch_eh.py loads headlessly every night.
Re-run this whenever the nightly log says the EH session expired.
"""
import pathlib, sys
from playwright.sync_api import sync_playwright

STATE = pathlib.Path.home() / ".config" / "wesandwoodward" / "eh_state.json"
STATE.parent.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    ctx = browser.new_context()
    page = ctx.new_page()
    page.goto("https://evolving-hockey.com/login/", wait_until="domcontentloaded")
    print("Log in to Evolving-Hockey in the window that opened, then press Enter here.")
    try:
        input()
    except EOFError:
        pass
    ctx.storage_state(path=str(STATE))
    browser.close()
print(f"saved {STATE}")
