#!/bin/zsh
# Full data refresh: raw pulls + site-ready JSON build.
# During the season, run nightly (launchd) and follow with a git push so the
# GitHub Actions build redeploys the Astro site with fresh data.
set -e
cd "$(dirname "$0")"
python3 pipeline/fetch_nhl.py
python3 pipeline/fetch_moneypuck.py
python3 pipeline/build_site_data.py
echo "refresh complete: $(date)"
