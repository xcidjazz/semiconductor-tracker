"""
Fetch 2y+ price history for the entire semi universe and compute returns.
"""
import sys, json, time
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd
from universe import UNIVERSE, get_all_tickers


def calc_return(series: pd.Series, days_back: int) -> float | None:
    """% return between latest close and the close ~days_back trading days back.

    Uses calendar days (>= days_back ago) and finds the closest available close.
    Returns None if insufficient history.
    """
    if series is None or len(series) < 2:
        return None
    s = series.dropna()
    if len(s) < 2:
        return None
    latest = s.iloc[-1]
    target_date = s.index[-1] - pd.Timedelta(days=days_back)
    # Use the last close on or before target_date
    older = s[s.index <= target_date]
    if len(older) == 0:
        return None
    old_px = older.iloc[-1]
    if old_px == 0 or pd.isna(old_px):
        return None
    return float((latest / old_px - 1) * 100)


def ytd_return(series: pd.Series) -> float | None:
    if series is None or len(series) < 2:
        return None
    s = series.dropna()
    if len(s) < 2:
        return None
    latest = s.iloc[-1]
    latest_year = s.index[-1].year
    # Last close of prior year
    prior = s[s.index.year < latest_year]
    if len(prior) == 0:
        return None
    old_px = prior.iloc[-1]
    if old_px == 0 or pd.isna(old_px):
        return None
    return float((latest / old_px - 1) * 100)


def fetch_one(ticker: str):
    """Fetch a single ticker. Returns dict or None on failure."""
    try:
        t = yf.Ticker(ticker)
        # 3y of daily data (gives buffer for 2Y lookback)
        hist = t.history(period="3y", auto_adjust=True)
        if hist is None or len(hist) < 5:
            return None
        close = hist["Close"]
        try:
            info = t.fast_info
            currency = getattr(info, "currency", None) or "USD"
        except Exception:
            currency = "USD"
        latest = float(close.iloc[-1])
        return {
            "price": latest,
            "currency": currency,
            "d1": calc_return(close, 1),
            "d7": calc_return(close, 7),
            "d14": calc_return(close, 14),
            "m1": calc_return(close, 30),
            "m3": calc_return(close, 90),
            "ytd": ytd_return(close),
            "y1": calc_return(close, 365),
            "y2": calc_return(close, 730),
            "as_of": str(close.index[-1].date()),
        }
    except Exception as e:
        print(f"  ERROR {ticker}: {e}", file=sys.stderr)
        return None


def main():
    all_tickers = get_all_tickers()
    print(f"Fetching {len(all_tickers)} tickers...", file=sys.stderr)
    results = []
    failed = []
    for i, (tkr, name, country, cat) in enumerate(all_tickers, 1):
        data = fetch_one(tkr)
        if data is None:
            failed.append(tkr)
            print(f"[{i}/{len(all_tickers)}] {tkr:14s} FAILED", file=sys.stderr)
            continue
        row = {
            "ticker": tkr,
            "name": name,
            "country": country,
            "category": cat,
            **data,
        }
        results.append(row)
        if i % 20 == 0:
            print(f"[{i}/{len(all_tickers)}] {tkr:14s} ${data['price']:.2f}", file=sys.stderr)

    print(f"\nDone. Success: {len(results)}, Failed: {len(failed)}", file=sys.stderr)
    if failed:
        print(f"Failed tickers: {failed}", file=sys.stderr)

    output = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "rows": results,
        "failed": failed,
    }
    with open("data.json", "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"Wrote data.json with {len(results)} rows", file=sys.stderr)


if __name__ == "__main__":
    main()
