# Setup Checklist — Run on Your Personal Computer

A step-by-step you can work through. Should take 15-20 minutes start to finish.

## Step 0 — Download all the files

Download the entire `semiconductor_tracker` folder from this chat. **Important:** make sure you get the hidden `.github/` folder too — that's the GitHub Actions workflow that makes the daily auto-refresh work.

After download, your folder should contain:
```
semiconductor_tracker/
├── HANDOFF.md          ← paste this into your other Claude (see Step 1)
├── SETUP.md            ← this file
├── README.md
├── universe.py
├── fetch_data.py
├── build_dashboard.py
├── retag.py
├── refresh.sh
├── requirements.txt
├── data.json
├── semiconductor_tracker.html
├── .gitignore
└── .github/
    └── workflows/
        └── refresh.yml
```

If you don't see `.github/` after extracting, your zip tool may be hiding dotfiles. On macOS: `Cmd+Shift+.` in Finder to show them. On Windows: View tab → check "Hidden items" in File Explorer.

## Step 1 — Brief your personal Claude

In your other Claude account, start a **new conversation** and paste the entire contents of `HANDOFF.md` as your first message. That gives it the full context of what's been built, the design decisions made, known issues, and likely next steps. After that you can just ask it to help you with anything — extending categories, debugging, deploying, etc.

## Step 2 — Test it locally (5 min)

Make sure Python 3.11+ is installed:
```bash
python3 --version
```

If not, install from python.org (or `brew install python` on macOS, or `winget install Python.Python.3.11` on Windows).

Then in your terminal:
```bash
cd path/to/semiconductor_tracker
pip install -r requirements.txt
```

Open `semiconductor_tracker.html` in any browser — it should work immediately with the snapshot data that's already in `data.json`.

If you want a fresh refresh right now:
```bash
./refresh.sh
```
(On Windows: `python fetch_data.py` then `python build_dashboard.py`)

Takes about 2-3 minutes.

## Step 3 — Push to GitHub (5 min)

Create a new repo on github.com — public or private, both work. Don't initialize it with a README (you already have one).

Back in the terminal:
```bash
cd path/to/semiconductor_tracker
git init
git add .                # the dot is important - picks up hidden .github folder
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

Verify on github.com that the `.github/workflows/refresh.yml` file is there. If it's missing, the daily refresh won't work.

## Step 4 — Enable GitHub Pages (2 min)

1. Repo → **Settings** tab → **Pages** in left sidebar
2. Source: **Deploy from a branch**
3. Branch: **main**, Folder: **/ (root)** → Save

Wait ~1 minute. Your dashboard URL:
```
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/semiconductor_tracker.html
```

(GitHub will also show the URL at the top of the Pages settings page after deployment.)

## Step 5 — Enable Actions write permissions (1 min)

**This is the step most people forget — without it, the daily refresh can't commit back to your repo.**

1. Repo → **Settings** → **Actions** → **General**
2. Scroll down to **Workflow permissions**
3. Select **Read and write permissions**
4. Save

## Step 6 — Test the daily refresh workflow (3 min)

1. Repo → **Actions** tab
2. Click **Daily Refresh** in the left sidebar
3. Click **Run workflow** dropdown → **Run workflow** (use main branch)
4. Wait ~3 minutes. The run should show green.
5. Check your repo's commit log — you should see a new commit from `github-actions[bot]` updating `data.json` and `semiconductor_tracker.html`.

If it fails:
- **Permission denied / 403:** Step 5 wasn't done correctly. Re-check.
- **Yahoo Finance 429 / rate limit:** edit `fetch_data.py`, add `time.sleep(0.3)` inside the for-loop in `main()`. Commit and re-run.
- **Other errors:** click the failed step in the Actions log to see the traceback. Paste it to your Claude.

## Step 7 — Done

From this point forward, the workflow runs automatically Mon-Fri at 22:00 UTC (after US market close). Your Pages URL will always show the latest snapshot. Bookmark it.

To change the schedule, edit the cron line in `.github/workflows/refresh.yml`:
```yaml
- cron: '0 22 * * 1-5'   # current: weekdays 22:00 UTC
- cron: '0 13 * * 1-5'   # alternative: 9am US Eastern (pre-market)
- cron: '0 22 * * *'     # alternative: every day including weekends
```

Cron is UTC. Use [crontab.guru](https://crontab.guru/) to sanity-check.

---

## When you want to extend or modify

The single most important file is `universe.py`. Add tickers, split categories, rename anything. After editing:

```bash
python3 retag.py              # fast: re-categorize without re-fetching
python3 build_dashboard.py    # rebuild the HTML
git add . && git commit -m "Update universe" && git push
```

GitHub Pages auto-updates within ~1 minute of push.

For anything more complex than a universe edit, **ask your other Claude** with the HANDOFF.md context loaded. It'll know what's going on.
