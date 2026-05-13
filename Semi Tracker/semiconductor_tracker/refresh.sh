#!/usr/bin/env bash
# Daily refresh: pull fresh prices, rebuild dashboard, open it.
# Usage:  ./refresh.sh
set -e
cd "$(dirname "$0")"
echo "→ Fetching fresh prices (this takes ~2-3 minutes for ~190 tickers)..."
python3 fetch_data.py
echo ""
echo "→ Rebuilding dashboard..."
python3 build_dashboard.py
echo ""
echo "✓ Done. Open semiconductor_tracker.html in your browser."
