"""
Comprehensive Semiconductor Stock Universe
Organized by supply-chain layer / business model.

Format: (ticker, company name, country)
"""

UNIVERSE = {
    "Lithography Equipment": [
        ("ASML", "ASML Holding", "NL"),
        ("7751.T", "Canon", "JP"),
        ("7731.T", "Nikon", "JP"),
        ("SMHN.DE", "SUSS MicroTec", "DE"),
        ("6920.T", "Lasertec (EUV mask inspection)", "JP"),
    ],

    "WFE — Diversified Majors (multi-process)": [
        ("AMAT", "Applied Materials (depo/etch/CMP/implant)", "US"),
        ("LRCX", "Lam Research (etch + depo)", "US"),
        ("8035.T", "Tokyo Electron (track/etch/clean/depo)", "JP"),
    ],

    "WFE — Deposition (ALD / CVD / Thermal)": [
        ("ASM.AS", "ASM International (ALD leader)", "NL"),
        ("6525.T", "Kokusai Electric (thermal/batch ALD)", "JP"),
        ("688135.SS", "Piotech (CN deposition)", "CN"),
    ],

    "WFE — Etch (Specialists)": [
        ("688012.SS", "AMEC (CN etch leader)", "CN"),
    ],

    "WFE — Diversified China": [
        ("002371.SZ", "Naura Technology (etch+depo+thermal)", "CN"),
    ],

    "WFE — Process Control / Metrology / Inspection": [
        ("KLAC", "KLA Corp (process control leader)", "US"),
        ("ONTO", "Onto Innovation (metrology)", "US"),
        ("CAMT", "Camtek (adv packaging metrology)", "IL"),
        ("PRCH", "Park Systems (AFM metrology)", "KR"),
    ],

    "WFE — Wafer Cleaning": [
        ("7735.T", "Screen Holdings (cleaning + track)", "JP"),
        ("ACMR", "ACM Research (wafer cleaning)", "US"),
        ("688120.SS", "Hwatsing (CN cleaning)", "CN"),
    ],

    "WFE — Track (Coater / Developer)": [
        ("688037.SS", "Kingsemi (CN track tools)", "CN"),
    ],

    "WFE — Ion Implantation": [
        ("ACLS", "Axcelis Technologies", "US"),
    ],

    "WFE — MOCVD / Epitaxy / Compound Semi Tools": [
        ("VECO", "Veeco Instruments (MOCVD)", "US"),
        ("AIXA.DE", "AIXTRON (MOCVD)", "DE"),
    ],

    "WFE — Advanced Packaging / Hybrid Bonding": [
        ("BESI.AS", "BE Semiconductor (hybrid bonding)", "NL"),
        ("KLIC", "Kulicke & Soffa (wire/flip-chip bond)", "US"),
    ],

    "WFE — Laser Processing & Dicing": [
        ("LPK.DE", "LPKF Laser & Electronics", "DE"),
    ],

    "WFE — Subsystems & Subfab Components": [
        ("MKSI", "MKS Instruments (vacuum/gas/RF)", "US"),
        ("AEIS", "Advanced Energy (power conversion)", "US"),
        ("ENTG", "Entegris (fluid/materials handling)", "US"),
        ("AZTA", "Azenta / Brooks (wafer automation)", "US"),
        ("UCTT", "Ultra Clean Holdings (subsystems)", "US"),
        ("ICHR", "Ichor Holdings (subsystems)", "US"),
    ],

    "WFE — Fab Automation / Wafer Handling": [
        ("6383.T", "Daifuku (clean-fab AMHS)", "JP"),
    ],

    "Test & Inspection Equipment": [
        ("TER", "Teradyne", "US"),
        ("6857.T", "Advantest", "JP"),
        ("COHU", "Cohu (handlers)", "US"),
        ("FORM", "FormFactor (probe cards)", "US"),
        ("AEHR", "Aehr Test Systems", "US"),
        ("INTT", "inTEST", "US"),
        ("KEYS", "Keysight Technologies", "US"),
        ("2449.TW", "King Yuan Electronics", "TW"),
        ("3454.TW", "Test Research Inc (TFC)", "TW"),
    ],

    "Photomasks": [
        ("PLAB", "Photronics", "US"),
        ("7911.T", "Toppan Holdings", "JP"),
        ("7912.T", "Dai Nippon Printing", "JP"),
        ("7741.T", "Hoya Corp (mask blanks)", "JP"),
        ("5201.T", "AGC Inc (mask blanks)", "JP"),
    ],

    "Photoresist & Process Chemicals": [
        ("4186.T", "Tokyo Ohka Kogyo (TOK)", "JP"),
        ("4063.T", "Shin-Etsu Chemical", "JP"),
        ("4005.T", "Sumitomo Chemical", "JP"),
        ("4901.T", "Fujifilm Holdings", "JP"),
        ("MRK.DE", "Merck KGaA", "DE"),
        ("DD", "DuPont", "US"),
        ("AVTR", "Avantor", "US"),
        ("5384.T", "Fujimi (CMP slurries)", "JP"),
        ("ESI", "Element Solutions", "US"),
        ("4183.T", "Mitsui Chemicals (EUV pellicles)", "JP"),
        ("4188.T", "Mitsubishi Chemical", "JP"),
    ],

    "Specialty Gases": [
        ("LIN", "Linde", "GB"),
        ("APD", "Air Products & Chemicals", "US"),
        ("AI.PA", "Air Liquide", "FR"),
        ("4091.T", "Nippon Sanso (Taiyo Nippon)", "JP"),
        ("4004.T", "Resonac (Showa Denko)", "JP"),
        ("8088.T", "Iwatani Corp", "JP"),
        ("ICL", "ICL Group (bromine)", "IL"),
    ],

    "Silicon Wafers": [
        ("3436.T", "SUMCO", "JP"),
        ("WAF.DE", "Siltronic", "DE"),
        ("6488.TW", "GlobalWafers", "TW"),
        ("SOI.PA", "Soitec", "FR"),
        ("6182.TW", "Wafer Works", "TW"),
    ],

    "ABF Substrates & Carriers": [
        ("4062.T", "Ibiden", "JP"),
        ("6967.T", "Shinko Electric Industries", "JP"),
        ("3037.TW", "Unimicron Technology", "TW"),
        ("3189.TW", "Kinsus Interconnect", "TW"),
        ("ATS.VI", "AT&S Austria", "AT"),
        ("8046.TW", "Nan Ya PCB", "TW"),
        ("036710.KS", "Simmtech", "KR"),
        ("011070.KS", "LG Innotek", "KR"),
        ("009150.KS", "Samsung Electro-Mechanics", "KR"),
        ("2802.T", "Ajinomoto (ABF film)", "JP"),
    ],

    "Foundries (Pure-play)": [
        ("TSM", "TSMC (ADR)", "TW"),
        ("2330.TW", "TSMC (Taiwan)", "TW"),
        ("UMC", "UMC (ADR)", "TW"),
        ("2303.TW", "UMC (Taiwan)", "TW"),
        ("GFS", "GlobalFoundries", "US"),
        ("0981.HK", "SMIC (HK)", "CN"),
        ("688981.SS", "SMIC (Shanghai)", "CN"),
        ("1347.HK", "Hua Hong Semi (HK)", "CN"),
        ("688347.SS", "Hua Hong Semi (Shanghai)", "CN"),
        ("5347.TW", "Vanguard International Semi", "TW"),
        ("6770.TW", "Powerchip (PSMC)", "TW"),
        ("TSEM", "Tower Semiconductor", "IL"),
    ],

    "IDMs - Analog/Auto/Industrial": [
        ("TXN", "Texas Instruments", "US"),
        ("ADI", "Analog Devices", "US"),
        ("STM", "STMicroelectronics (NYSE)", "FR"),
        ("IFX.DE", "Infineon Technologies", "DE"),
        ("NXPI", "NXP Semiconductors", "NL"),
        ("6723.T", "Renesas Electronics", "JP"),
        ("ON", "onsemi", "US"),
        ("MCHP", "Microchip Technology", "US"),
        ("AMS.SW", "ams OSRAM", "CH"),
        ("VSH", "Vishay Intertechnology", "US"),
        ("DIOD", "Diodes Inc", "US"),
        ("6963.T", "ROHM", "JP"),
        ("WOLF", "Wolfspeed (SiC)", "US"),
    ],

    "Memory — HBM / Diversified DRAM+NAND+HBM": [
        ("000660.KS", "SK Hynix (HBM leader)", "KR"),
        ("MU", "Micron Technology", "US"),
        ("005930.KS", "Samsung Electronics (memory+foundry)", "KR"),
    ],

    "Memory — NAND Pure-play": [
        ("285A.T", "Kioxia Holdings", "JP"),
        ("SNDK", "Sandisk", "US"),
    ],

    "Memory — DRAM Pure-play (specialty/legacy)": [
        ("2408.TW", "Nanya Technology (DRAM)", "TW"),
    ],

    "Memory — NOR Flash / Niche": [
        ("2337.TW", "Macronix International (NOR/NAND)", "TW"),
        ("2344.TW", "Winbond Electronics (DRAM/NOR)", "TW"),
        ("603986.SS", "GigaDevice (NOR/MCU)", "CN"),
    ],

    "Storage — HDD / Drives / Systems": [
        ("WDC", "Western Digital (HDD)", "US"),
        ("STX", "Seagate Technology (HDD)", "US"),
        ("PSTG", "Pure Storage (SSD systems)", "US"),
        ("NTAP", "NetApp (storage systems)", "US"),
    ],

    "Compute — GPU": [
        ("NVDA", "NVIDIA (GPU dominator)", "US"),
    ],

    "Compute — CPU (Intel / AMD / ARM)": [
        ("INTC", "Intel (x86 CPU + IDM)", "US"),
        ("AMD", "AMD (x86 CPU + GPU)", "US"),
        ("ARM", "Arm Holdings (CPU IP)", "GB"),
    ],

    "Compute — Mobile/Client SoC": [
        ("QCOM", "Qualcomm (mobile SoC + modem)", "US"),
        ("2454.TW", "MediaTek (mobile SoC)", "TW"),
    ],

    "Compute — Custom ASIC / Hyperscaler Silicon": [
        ("AVGO", "Broadcom (Google TPU, Meta MTIA)", "US"),
        ("MRVL", "Marvell (AWS Trainium, custom)", "US"),
        ("3661.TW", "Alchip Technologies (ASIC design)", "TW"),
        ("3443.TW", "Global Unichip / GUC (ASIC)", "TW"),
        ("3035.TW", "Faraday Technology (ASIC)", "TW"),
    ],

    "Compute — AI Networking / Connectivity IC": [
        ("ALAB", "Astera Labs (PCIe/CXL retimers)", "US"),
        ("CRDO", "Credo Technology (SerDes/AECs)", "US"),
        ("ANET", "Arista Networks (data center switches)", "US"),
    ],

    "Compute — FPGA / Programmable": [
        ("LSCC", "Lattice Semiconductor (FPGA)", "US"),
    ],

    "Compute — Chip IP / RISC-V": [
        ("RMBS", "Rambus (memory + security IP)", "US"),
        ("CEVA", "CEVA (DSP/AI IP)", "US"),
        ("6533.TW", "Andes Technology (RISC-V IP)", "TW"),
        ("AWE.L", "Alphawave IP Group (SerDes IP)", "GB"),
    ],

    "Compute — AI Edge / Smart Sensors": [
        ("AMBA", "Ambarella (edge AI vision)", "US"),
        ("SLAB", "Silicon Labs (IoT)", "US"),
        ("SYNA", "Synaptics (HMI + edge)", "US"),
        ("SITM", "SiTime (precision timing)", "US"),
        ("CRUS", "Cirrus Logic (audio)", "US"),
    ],

    "Analog / Power / RF (Fabless)": [
        ("MPWR", "Monolithic Power Systems (power)", "US"),
        ("ALGM", "Allegro MicroSystems (sensors/power)", "US"),
        ("POWI", "Power Integrations (AC-DC)", "US"),
        ("NVTS", "Navitas (GaN power)", "US"),
        ("VICR", "Vicor Corp (power modules)", "US"),
        ("SWKS", "Skyworks Solutions (RF/PA)", "US"),
        ("QRVO", "Qorvo (RF/PA)", "US"),
        ("MTSI", "MACOM Technology (RF/optical)", "US"),
        ("SMTC", "Semtech (LoRa/analog)", "US"),
    ],

    "OSAT (Outsourced Assembly & Test)": [
        ("ASX", "ASE Technology (ADR)", "TW"),
        ("3711.TW", "ASE Technology (TW)", "TW"),
        ("AMKR", "Amkor Technology", "US"),
        ("0522.HK", "ASMPT", "HK"),
        ("6239.TW", "Powertech Technology", "TW"),
        ("IMOS", "ChipMOS Technologies", "TW"),
        ("600584.SS", "JCET Group", "CN"),
        ("002156.SZ", "Tongfu Microelectronics", "CN"),
        ("002185.SZ", "Tianshui Huatian Tech", "CN"),
    ],

    "Networking / Optical / Photonics": [
        ("COHR", "Coherent Corp", "US"),
        ("LITE", "Lumentum Holdings", "US"),
        ("POET", "POET Technologies", "CA"),
        ("AAOI", "Applied Optoelectronics", "US"),
        ("ANET", "Arista Networks", "US"),
        ("CIEN", "Ciena Corp", "US"),
        ("CSCO", "Cisco Systems", "US"),
        ("300308.SZ", "Innolight", "CN"),
        ("002281.SZ", "Accelink Technologies", "CN"),
        ("NPTN", "NeoPhotonics", "US"),
        ("INFN", "Infinera (Nokia)", "US"),
        ("FN", "Fabrinet", "US"),
    ],

    "EDA & Chip Design Tools": [
        ("SNPS", "Synopsys", "US"),
        ("CDNS", "Cadence Design Systems", "US"),
        ("ANSS", "Ansys", "US"),
        ("KEYS", "Keysight Technologies", "US"),
    ],

    "China Domestic Chip Plays": [
        ("002371.SZ", "Naura Tech", "CN"),
        ("688012.SS", "AMEC", "CN"),
        ("300782.SZ", "Maxscend Microelectronics", "CN"),
        ("603501.SS", "Will Semiconductor", "CN"),
        ("600703.SS", "Sanan Optoelectronics", "CN"),
        ("603986.SS", "GigaDevice Semiconductor", "CN"),
        ("688008.SS", "Montage Technology", "CN"),
        ("688256.SS", "Cambricon Technologies", "CN"),
    ],

    "Power/Compound Semi (SiC/GaN)": [
        ("002475.SZ", "Luxshare Precision", "CN"),
        ("6503.T", "Mitsubishi Electric", "JP"),
    ],

    "Infrastructure / Data Center Adjacent": [
        ("VRT", "Vertiv Holdings (cooling/power)", "US"),
        ("ETN", "Eaton Corp", "US"),
        ("ABBNY", "ABB Ltd", "CH"),
        ("SU.PA", "Schneider Electric", "FR"),
        ("MOD", "Modine Manufacturing", "US"),
        ("SMCI", "Super Micro Computer", "US"),
        ("DELL", "Dell Technologies", "US"),
        ("HPE", "Hewlett Packard Enterprise", "US"),
    ],

    "Indices / ETFs (Benchmarks)": [
        ("SOXX", "iShares Semiconductor ETF", "US"),
        ("SMH", "VanEck Semiconductor ETF", "US"),
        ("SOXL", "Direxion Semi Bull 3X", "US"),
        ("XSD", "SPDR S&P Semiconductor ETF", "US"),
        ("PSI", "Invesco Dynamic Semis ETF", "US"),
    ],
}


def get_all_tickers():
    """Return flat list of (ticker, name, country, category) tuples, deduplicated by ticker."""
    seen = set()
    out = []
    for cat, names in UNIVERSE.items():
        for tkr, name, country in names:
            if tkr in seen:
                continue
            seen.add(tkr)
            out.append((tkr, name, country, cat))
    return out


if __name__ == "__main__":
    all_t = get_all_tickers()
    print(f"Total unique tickers: {len(all_t)}")
    for cat in UNIVERSE:
        n = len(UNIVERSE[cat])
        print(f"  {cat}: {n}")
