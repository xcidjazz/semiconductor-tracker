"""Re-tag categories on existing data.json using current universe.py mapping.
Faster than re-fetching when only categories change."""
import json
from universe import get_all_tickers

# Build ticker -> (name, country, category) map from current universe
mapping = {tkr: (name, country, cat) for tkr, name, country, cat in get_all_tickers()}

with open("data.json") as f:
    data = json.load(f)

retagged = 0
dropped = 0
new_rows = []
for r in data["rows"]:
    tkr = r["ticker"]
    if tkr in mapping:
        name, country, cat = mapping[tkr]
        r["name"] = name
        r["country"] = country
        r["category"] = cat
        retagged += 1
        new_rows.append(r)
    else:
        # Ticker no longer in universe — drop it
        print(f"  Dropping {tkr} (no longer in universe)")
        dropped += 1

# Add any new tickers that don't yet have data
existing_tkrs = {r["ticker"] for r in new_rows}
new_tickers = [(t, n, c, cat) for t, (n, c, cat) in mapping.items() if t not in existing_tkrs]
if new_tickers:
    print(f"  {len(new_tickers)} new tickers need fetching: {[t[0] for t in new_tickers]}")

data["rows"] = new_rows
with open("data.json", "w") as f:
    json.dump(data, f, indent=2, default=str)
print(f"Re-tagged {retagged} rows, dropped {dropped}, {len(new_tickers)} new tickers pending fetch")
