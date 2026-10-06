#!/bin/zsh
# Nightly stats refresh (launchd, 10:30 PM Pacific): pull NHL + MoneyPuck, rebuild team/site data and
# every player page, commit the data and push as markwesley622 so GitHub Actions redeploys the site.
# Evolving-Hockey exports are subscriber files that stay local, which is why this runs on the Mac, not in CI.
# It runs from the mirror clone at ~/.wesandwoodward/repo: launchd cannot read ~/Documents (macOS privacy
# protection), so the working copy in Documents just needs a `git pull` before Mark's own edits.
set -e
export PATH="/opt/homebrew/bin:/usr/local/bin:/Library/Frameworks/Python.framework/Versions/3.13/bin:$PATH"
cd "$(dirname "$0")/.."
LOG="$HOME/.wesandwoodward/logs/nightly-$(date +%Y-%m-%d).log"
{
  echo "=== nightly start $(date)"
  git pull -q --ff-only origin main
  ./refresh.sh
  python3 pipeline/fetch_eh.py || echo "EH pull failed, continuing with the files on disk"
  python3 pipeline/build_player.py --roster --fetch
  # prospect system: re-applies the status rule and roster-status template swap on the cached EliteProspects
  # pull (data/raw/ep, refreshed by hand from Mark's Chrome via pipeline/ep_refresh.py; it is not in git)
  python3 pipeline/build_prospects.py || echo "prospect build failed, keeping the files on disk"
  npm run build --silent >/dev/null
  git add -A data/site data/archive data/raw/nhl data/raw/moneypuck data/raw/players
  if git diff --cached --quiet; then
    echo "no data changes"
  else
    git -c user.name="Mark Wesley" -c user.email="31449404+markwesley622@users.noreply.github.com" commit -q -m "Nightly stats refresh $(date +%Y-%m-%d)"
    TOKEN="$(gh auth token -u markwesley622)"
    git push -q "https://x-access-token:${TOKEN}@github.com/markwesley622/wes-and-woodward.git" HEAD:main
    echo "pushed $(git rev-parse --short HEAD)"
  fi
  echo "=== nightly done $(date)"
} >> "$LOG" 2>&1
