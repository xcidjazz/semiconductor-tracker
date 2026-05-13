# Project Handoff — Semiconductor Universe Tracker

Hi Claude. The user is continuing a project that was started in another Claude conversation. This document gives you the context you need to help them.

## TL;DR

The user wants a **daily-refreshing performance dashboard** for the global public semiconductor universe, organized by supply-chain process (litho, etch, deposition, photoresist, HBM, NAND, CPU, GPU, etc.). It's a folder of Python + a self-contained HTML file. The plan is to host it on **GitHub Pages with a GitHub Actions workflow that refreshes the data every weekday after US market close.**

Treat this as a working project. The user wants pragmatic help — extending categories, debugging deployment, adding features, sanity-checking design choices.

---

## What's already built

**Universe:** ~187 public semi-related tickers across ~45 fine-grained categories. Major buckets and their granular splits:

- **Lithography Equipment** (5): ASML, Canon, Nikon, SUSS, Lasertec
- **WFE — Diversified Majors (multi-process)** (3): AMAT, LRCX, Tokyo Electron
- **WFE — Deposition (ALD/CVD/Thermal)** (3): ASM International, Kokusai, Piotech
- **WFE — Etch (Specialists)** (1): AMEC (CN)
- **WFE — Process Control / Metrology / Inspection** (4): KLA, Onto, Camtek, Park Systems
- **WFE — Wafer Cleaning** (3): Screen Holdings, ACM Research, Hwatsing
- **WFE — Track (Coater/Developer)** (1): Kingsemi
- **WFE — Ion Implantation** (1): Axcelis
- **WFE — MOCVD / Epitaxy / Compound Semi Tools** (2): Veeco, AIXTRON
- **WFE — Advanced Packaging / Hybrid Bonding** (2): BESI, Kulicke & Soffa
- **WFE — Laser Processing & Dicing** (1): LPKF
- **WFE — Subsystems & Subfab Components** (6): MKS, AEIS, Entegris, Azenta, UCTT, Ichor
- **WFE — Fab Automation / Wafer Handling** (1): Daifuku
- **WFE — Diversified China** (1): Naura
- **Test & Inspection Equipment** (9): Teradyne, Advantest, Cohu, FormFactor, Aehr, inTEST, Keysight, King Yuan, TFC
- **Photomasks** (5): Photronics, Toppan, DNP, Hoya, AGC
- **Photoresist & Process Chemicals** (11): TOK, Shin-Etsu Chemical, Sumitomo Chemical, Fujifilm, Merck KGaA, DuPont, Avantor, Fujimi, Element Solutions, Mitsui Chemicals, Mitsubishi Chemical
- **Specialty Gases** (7): Linde, Air Products, Air Liquide, Nippon Sanso, Resonac, Iwatani, ICL
- **Silicon Wafers** (5): SUMCO, Siltronic, GlobalWafers, Soitec, Wafer Works
- **ABF Substrates & Carriers** (10): Ibiden, Shinko Electric, Unimicron, Kinsus, AT&S, Nan Ya PCB, Simmtech, LG Innotek, Samsung Electro-Mechanics, Ajinomoto
- **Foundries (Pure-play)** (12): TSMC (ADR + TW), UMC, GlobalFoundries, SMIC (HK + Shanghai), Hua Hong, Vanguard, PSMC, Tower Semi
- **IDMs — Analog/Auto/Industrial** (13): TXN, ADI, STM, Infineon, NXP, Renesas, onsemi, Microchip, ams OSRAM, Vishay, Diodes, ROHM, Wolfspeed
- **Memory — HBM / Diversified DRAM+NAND+HBM** (3): SK Hynix, Micron, Samsung
- **Memory — NAND Pure-play** (2): Kioxia, Sandisk
- **Memory — DRAM Pure-play (specialty/legacy)** (1): Nanya Tech
- **Memory — NOR Flash / Niche** (3): Macronix, Winbond, GigaDevice
- **Storage — HDD / Drives / Systems** (4): WDC, Seagate, Pure Storage, NetApp
- **Compute — GPU** (1): NVIDIA
- **Compute — CPU (Intel / AMD / ARM)** (3): Intel, AMD, ARM
- **Compute — Mobile/Client SoC** (2): Qualcomm, MediaTek
- **Compute — Custom ASIC / Hyperscaler Silicon** (5): Broadcom, Marvell, Alchip, GUC, Faraday
- **Compute — AI Networking / Connectivity IC** (3): Astera Labs, Credo, Arista
- **Compute — FPGA / Programmable** (1): Lattice
- **Compute — Chip IP / RISC-V** (4): Rambus, CEVA, Andes, Alphawave
- **Compute — AI Edge / Smart Sensors** (5): Ambarella, Silicon Labs, Synaptics, SiTime, Cirrus
- **Analog / Power / RF (Fabless)** (9): MPWR, ALGM, POWI, Navitas, Vicor, Skyworks, Qorvo, MACOM, Semtech
- **OSAT (Outsourced Assembly & Test)** (9): ASE (ADR + TW), Amkor, ASMPT, Powertech, ChipMOS, JCET, Tongfu, Tianshui Huatian
- **Networking / Optical / Photonics** (12): Coherent, Lumentum, POET, AAOI, Arista, Ciena, Cisco, Innolight, Accelink, NeoPhotonics, Infinera, Fabrinet
- **EDA & Chip Design Tools** (4): Synopsys, Cadence, Ansys, Keysight
- **China Domestic Chip Plays** (8): Naura, AMEC, Maxscend, Will Semi, Sanan, GigaDevice, Montage, Cambricon
- **Power/Compound Semi (SiC/GaN)** (2): Luxshare, Mitsubishi Electric
- **Infrastructure / Data Center Adjacent** (8): Vertiv, Eaton, ABB, Schneider, Modine, SMCI, Dell, HPE
- **Indices / ETFs (Benchmarks)** (5): SOXX, SMH, SOXL, XSD, PSI

**Returns calculated for each ticker:** 1D, 1W, 2W, 1M, 3M, YTD, 1Y, 2Y — split- and dividend-adjusted, in local currency. Calendar-day based (looks back N days, finds closest close on or before).

## Tech stack

- **Data source:** Yahoo Finance via the `yfinance` Python library
- **Language:** Python 3.11 for fetch/build, vanilla JS for the dashboard interactions
- **Output:** Single self-contained HTML file (`semiconductor_tracker.html`) with data embedded — no backend, runs from a file:// URL or static hosting
- **Hosting plan:** GitHub Pages serves the HTML, GitHub Actions runs the Python refresh script on cron (currently Mon-Fri 22:00 UTC)
- **Design:** Dark theme, Fraunces (italic display) + Manrope (body) + JetBrains Mono (numbers), heatmap-colored return cells, sticky header

## File layout

```
semiconductor_tracker/
├── universe.py              # Master ticker list, grouped by category. EDIT HERE.
├── fetch_data.py            # Pulls 3y prices from yfinance, computes returns, writes data.json (~3 min)
├── build_dashboard.py       # Reads data.json, generates semiconductor_tracker.html
├── retag.py                 # FAST: re-categorize without re-fetching. Use after editing universe.py
├── refresh.sh               # One-liner: ./refresh.sh runs fetch + build
├── requirements.txt         # yfinance + pandas
├── README.md                # Setup + deploy instructions
├── .gitignore
├── .github/workflows/refresh.yml   # GitHub Actions: daily auto-refresh
├── data.json                # Current snapshot (auto-generated)
└── semiconductor_tracker.html  # The dashboard (auto-generated)
```

## Dashboard features (so you don't have to re-derive them)

1. **Top movers strip** — biggest 1D up, biggest 1D down, best YTD, best 1Y across whole universe
2. **Sector heatmap** — median (default) or mean toggle, 1D/1W/2W/1M/3M/YTD/1Y/2Y columns, sortable by any timeframe, **rows are clickable to scroll to that category in the table below**
3. **Per-ticker table** — grouped by category, sortable per group, color-coded return cells, search box, category filter, region filter
4. **All in one HTML file** — no build step, no backend, works on any static host

## Design decisions made (so you don't re-litigate them)

- **Median used as default heatmap aggregate**, not mean — robust to single-stock outliers (Sandisk +4000% 1Y because of WDC spinoff). Mean is a toggle.
- **Calendar-day returns, not trading-day** — "1W" = 7 calendar days back, closest available close. Good enough for relative comparison, easier to explain.
- **Local currency, not USD-normalized** — explicitly flagged in the README as a known caveat. Adding FX normalization is a future option.
- **3y of history fetched** — gives enough buffer that 2Y lookback works for almost everything (only fails for very recent IPOs).
- **Diversified Majors kept as a single bucket** for AMAT/LRCX/TEL because they truly are multi-process. Don't try to split them by primary product — they're across all of etch/depo/clean/CMP/implant.
- **Some categories have N=1** (Axcelis in Ion Implantation, LPKF in Laser Processing). User is OK with this — they explicitly wanted granular. The sector signal is "watchlist on one name," not a real sector read.

## Known issues / gotchas

- **Acquired/delisted tickers** that yfinance can't find — currently silently skipped: NPTN (acquired by Lumentum), INFN (Nokia), ANSS (Synopsys), AWE.L (Qualcomm), Shinko Electric (JIC consortium), some Taiwan tickers with malformed codes. If user wants to track post-acquisition exposure, point them to the acquirer's ticker.
- **GitHub Actions + Yahoo Finance rate limits** — possible failure mode. If the cron run errors out with 429s, add `time.sleep(0.3)` between tickers in `fetch_data.py`, or swap to a proper API (Polygon, Tiingo, EOD Historical, Finnhub).
- **Currency mixed in display** — a Taiwan stock up 50% in TWD is not the same as +50% in USD. Returns are shown in listing currency, currency code in price cell.
- **Median is misleading at N=1 or N=2** — single-stock categories are really "one company's story," not a sector.

## What the user might ask you to do next

Likely:
- Add more tickers (point them to `universe.py`, run `retag.py` then `build_dashboard.py`)
- Add a new category split (edit `universe.py`, ticker first appearance wins, run retag)
- USD normalization for returns
- Add market cap, P/E, or other fundamentals (would require additional yfinance calls in fetch_data.py — `Ticker.info` has these but is rate-limited)
- Add charts (sparklines, sector rotation chart) — currently only tabular
- Swap yfinance for a proper API
- Debug GitHub Pages or Actions deployment failures
- Add a USD-converted column or FX toggle

Less likely but possible:
- Add fundamentals (revenue growth, gross margins)
- Add a watchlist / starring feature (would need browser localStorage — works fine on GitHub Pages)
- Email/Slack alerts on threshold moves

## How to refresh / extend

```bash
# Daily refresh (local)
./refresh.sh

# After editing universe.py (fast — no re-fetch)
python3 retag.py && python3 build_dashboard.py

# Full from scratch
python3 fetch_data.py && python3 build_dashboard.py
```

---

**Treat the user as someone who knows what they want and is iterating quickly. They like concise answers with concrete deliverables. Don't ask clarifying questions before doing work that's obvious — just do it and offer alternatives.**
