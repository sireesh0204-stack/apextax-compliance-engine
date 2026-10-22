# ⚡ ApexTax Compliance Engine — TY 2025 US Individual Tax Workstation & Mobile OS

[![Tax Year](https://img.shields.io/badge/Tax%20Year-2025%20Filing%20Season-blue.svg?style=flat-square)](https://www.irs.gov)
[![Engine](https://img.shields.io/badge/Engine-Deterministic%20IRC%20TypeScript-2b7489.svg?style=flat-square)](https://www.typescriptlang.org/)
[![Android](https://img.shields.io/badge/Android%20APK-API%2034%20(Debug%20Ready)-3DDC84.svg?style=flat-square&logo=android&logoColor=white)](https://developer.android.com/)
[![Shell](https://img.shields.io/badge/Shell-Capacitor%20v6%20Hybrid%20Native-119EFF.svg?style=flat-square&logo=capacitor&logoColor=white)](https://capacitorjs.com/)
[![Audit Workpapers](https://img.shields.io/badge/Workpapers-Big%204%20Lead%20Sheets-0052CC.svg?style=flat-square)](https://github.com/sireesh0204-stack/apextax-compliance-engine)
[![Latency](https://img.shields.io/badge/Calculation%20Latency-Sub--2ms%20(0ms%20Local)-brightgreen.svg?style=flat-square)](https://github.com/sireesh0204-stack/apextax-compliance-engine)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg?style=flat-square)](LICENSE)

An enterprise-grade, deterministic **Tax Year 2025 US Individual Income Tax (Form 1040) compliance engine**, paired with professional **Big 4 accounting workpaper lead sheets (`WP-1040`)**, client-side zero-dependency PDF stamping, and a native **Android `.apk` mobile hardware shell**.

Modeled after tier-1 professional tax preparation software (Intuit ProConnect, CCH Axcess, and Thomson Reuters UltraTax), **ApexTax** bridges the gap between statutory Internal Revenue Code (IRC) precision and production-grade tax-technology software engineering.

---

## 🏛️ Executive Summary & Author Positioning

> *"Most tax preparers know what buttons to click in tax software, but have zero insight into how the calculation engine executes underneath. Most software engineers write code for tax platforms without understanding the statutory ordering of loss waterfalls or why an XSD schema passes mathematically defective returns."*

**ApexTax** was authored by **Anasuri Sireesh Kumar**—former Senior Tax Analyst & Tax Form Implementation Engineer at Instead/Corvee (authored 400+ production Go calculation files across 27 state tax regimes, Form 1120-S, Form 7203, and MeF e-file schemas) and former US Tax Analyst at H&R Block (Blockworks TRC & DOR ATS lead).

This repository serves as a **flagship public technical showcase** demonstrating:
1. **Statutory Integrity**: Deterministic implementation of TY 2025 IRC calculation waterfalls (Section 199A QBID, Form 8582 PAL netting, Form 6251 AMT, Form 8960 NIIT, Form 7203 basis cascades, and Schedule A SALT phaseouts).
2. **Audit Workpaper Discipline**: Real Big 4 accounting lead sheets (`WP-1040-E`, `WP-1040-C`, `WP-1040-A`) featuring Book-to-Tax adjustments (M-1/M-3) and standardized audit tickmarks (`✓ Agreed to Slip`, `≠ Discrepancy Trap`, `∑ Footed`, `⨂ Cross-Footed`).
3. **Zero External Latency**: 100% offline, client-side mathematical execution (sub-2ms) and dynamic multi-page PDF slip generation via raw `pdf-lib` byte manipulation with **zero external CDN dependencies**.
4. **Unified Cross-Platform Core**: A single TypeScript/HTML engine deployed simultaneously as a **Desktop Multi-Monitor Workstation** and compiled into a **Native Android `.apk`** (Android SDK 34 / Java 17 LTS) via Ionic Capacitor with custom hardware bridges (`ApexHardwarePlugin.java`).

---

## 📐 System Architecture

ApexTax implements a reactive, unidirectional data flow that strictly isolates statutory mathematical computation from DOM rendering and native platform bridges:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                   INPUT SOURCES                                        │
│  ┌─────────────────────────┐  ┌─────────────────────────┐  ┌────────────────────────┐  │
│  │   Direct User Inputs    │  │  Multi-Page PDF Slips   │  │ Hardware Camera / OCR  │  │
│  │  (W-2, 1099, K-1, etc.) │  │  (Client-side pdf-lib)  │  │   & Speech-To-Text     │  │
│  └───────────┬─────────────┘  └───────────┬─────────────┘  └───────────┬────────────┘  │
└──────────────┼────────────────────────────┼────────────────────────────┼───────────────┘
               ▼                            ▼                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        STATUTORY CALCULATION ENGINE (TY 2025)                          │
│                                                                                        │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ 1. Gross Income Layer: Form 1040 L1–L9 • Schedule 1 Part I • Schedule B • Sch D  │  │
│  └────────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                           ▼                                            │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ 2. Loss Limitation Cascade: §704(d)/§1366 Basis (Form 7203) ──►                   │  │
│  │    §465 At-Risk (Form 6198) ──► §469 Passive Activity Loss (Form 8582) ──►       │  │
│  │    §461(l) Excess Business Loss Netting                                          │  │
│  └────────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                           ▼                                            │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ 3. Adjusted Gross Income (AGI) Layer: Form 1040 Line 11 • Schedule 1 Part II    │  │
│  │    (50% SE Tax Deduction §164(f) • IRA Deductions • SEHI)                        │  │
│  └────────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                           ▼                                            │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ 4. Deductions & Specialized Worksheets:                                          │  │
│  │    • Schedule A Line 5e SALT Phaseout ($40k Cap / 30% Reduction / $10k Floor)    │  │
│  │    • Standard Deduction vs. Itemized Comparison Engine                           │  │
│  │    • Section 199A Qualified Business Income Deduction (Form 8995-A SSTB Engine)   │  │
│  └────────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                           ▼                                            │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
│  │ 5. Tax Computation & Surtaxes:                                                   │  │
│  │    • Form 1040 Line 16 Preferential Capital Gain / Qualified Dividend Worksheet  │  │
│  │    • Form 6251 Alternative Minimum Tax (AMT Exemption Phaseout Engine)           │  │
│  │    • Form 8960 Net Investment Income Tax (3.8% Surtax on Net Investment Income)  │  │
│  │    • Schedule SE Self-Employment Tax (12.4% OASDI up to wage base + 2.9% HI)     │  │
│  └──────────────────────────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              PRESENTATION & OUTPUT PLATFORMS                           │
│                                                                                        │
│   ┌──────────────────────────┐  ┌──────────────────────────┐  ┌────────────────────┐   │
│   │ Desktop Tax Workstation  │  │ Big 4 Workpaper Engine   │  │ Native Android APK │   │
│   │ • 50/50 Live IRS PDF     │  │ • WP-1040-E Lead Sheet   │  │ • Capacitor v6     │   │
│   │ • Detachable Dual-Screen │  │ • WP-1040-C Lead Sheet   │  │ • API 34 Native    │   │
│   │ • AI Senior Reviewer     │  │ • WP-1040-A Lead Sheet   │  │ • Offline V8 Core  │   │
│   │ • NotebookLM Transmitter │  │ • Trial Balance & M-1    │  │ • Hardware TTS/STT │   │
│   └──────────────────────────┘  └──────────────────────────┘  └────────────────────┘   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## ⚖️ Statutory Calculation Engine (Tax Year 2025 Rules)

ApexTax strictly adheres to official IRS instructions, Treasury Regulations, and the Internal Revenue Code (IRC):

### 1. Multi-Tier Statutory Loss Limitation Cascade
Tax losses do not immediately reduce taxable income. The engine enforces the mandatory 4-tier statutory ordering:
1. **IRC §1366 / §704(d) Shareholder & Partner Basis Limitation (Form 7203)**: Losses are first throttled by stock and debt basis. Suspended basis losses are carried forward indefinitely.
2. **IRC §465 At-Risk Limitation (Form 6198)**: Allowed basis losses must be backed by capital at personal risk (including Qualified Nonrecourse Financing under §465(b)(6)).
3. **IRC §469 Passive Activity Loss Limitation (Form 8582)**:
   - Segregates active trade or business income from passive activities (rental real estate, limited partnerships).
   - Enforces the **$25,000 Special Active Participation Rental Allowance**, applying the statutory 50% phase-out between $100,000 and $150,000 MAGI.
   - Computes disallowed passive losses and accurately updates the unallowed loss carryforward schedule.
4. **IRC §461(l) Excess Business Loss (EBL) Limitation**: Remaining active business losses are subjected to the aggregate statutory cap ($305,000 Single / $610,000 Married Filing Jointly for TY 2025).

### 2. Form 1040 Line 16 Preferential Rate Tax Worksheet
Calculates federal regular tax liability using the official **25-Line Qualified Dividends and Capital Gain Tax Worksheet**:
- Segregates ordinary income taxed at progressive brackets (10%, 12%, 22%, 24%, 32%, 35%, 37%) from preferential income (qualified dividends and net long-term capital gains).
- Applies statutory 0%, 15%, and 20% capital gains rate thresholds based on taxable income tiers.

### 3. Schedule A State and Local Tax (SALT) Phaseout Engine
- Models the baseline statutory $40,000 deduction cap.
- Applies a **30% statutory reduction** on excess AGI above the $500,000 threshold while preserving the statutory $10,000 minimum floor.
- Automates the optimal comparison between standard deduction and itemized deductions.

### 4. IRC §199A Qualified Business Income Deduction (Form 8995-A)
- Full statutory engine for Specified Service Trades or Businesses (SSTB) and non-SSTBs.
- Implements the statutory phaseout thresholds for TY 2025 ($197,300 Single / $394,600 MFJ) over the $50,000 / $100,000 phaseout range.
- Enforces W-2 wage and Unadjusted Basis Immediately After Acquisition (UBIA) limitation tests.

### 5. Form 6251 Alternative Minimum Tax (AMT) & Form 8960 NIIT
- **Form 6251**: Dynamically computes Alternative Minimum Taxable Income (AMTI), adjusting for ISO bargain elements (Form 3921), and applies the statutory AMT exemption phaseout (25% reduction above $626,350 Single / $1,252,700 MFJ).
- **Form 8960**: Applies the **3.8% Net Investment Income Surtax** on the lesser of Net Investment Income (NII) or Modified Adjusted Gross Income (MAGI) over statutory threshold limits ($200,000 Single / $250,000 MFJ).

---

## 📋 Big 4 Accounting Workpaper System (`WP-1040`)

Professional tax compliance requires documented, auditable proof. ApexTax integrates a full **Lead Sheet Workpaper Drawer**:

```
WP-1040-E Lead Sheet (Supplemental Income & Loss)
┌──────────────────────┬─────────────────┬───────────────────┬───────────────────┐
│ Description          │ Unadjusted Book │ Audit Adjustments │ Federal Tax Total │
├──────────────────────┼─────────────────┼───────────────────┼───────────────────┤
│ Rental Properties    │   $45,000.00    │   -$12,500.00 (≠) │    $32,500.00 (✓) │
│ Partnerships / S-Corp│   $85,000.00    │   -$25,000.00 (≠) │    $60,000.00 (✓) │
│ Total Schedule E     │  $130,000.00    │   -$37,500.00 (≠) │    $92,500.00 (∑) │
└──────────────────────┴─────────────────┴───────────────────┴───────────────────┘
```

* **Lead Sheets Implemented**:
  * `WP-1040-E`: Supplemental Income & Loss (Rental Real Estate, Partnerships, S-Corporations, Estates, Trusts).
  * `WP-1040-C`: Profit or Loss From Business (Sole Proprietorship P&L, 1099-NEC tie-outs, Disallowed Entertainment M-1s).
  * `WP-1040-A`: Itemized Deductions (Medical, State & Local Taxes, Mortgage Interest Form 1098, Charitable Contributions).
* **Standardized Audit Tickmark Legend**:
  * `✓ Agreed`: Reconciled directly to source slip (W-2, 1099, K-1, Closing Statement).
  * `≠ Discrepancy Trap`: Audit alert flagged (e.g., 401(k) Box 1 vs Box 5 wage disparity, K-1 debt basis exhaustion).
  * `∑ Footed`: Vertically summed and verified.
  * `⨂ Cross-Footed`: Horizontally cross-checked and verified across schedules.

---

## 📱 Mobile OS & Native Android APK Architecture

ApexTax was engineered as an **offline-first hybrid native application** running on Android:

### Why Capacitor v6+ Shell over a Flutter/Compose Rewrite?
Porting a verified, multi-schedule tax engine and byte-precise `pdf-lib` form stamper into Dart or Kotlin creates statutory drift and duplicate maintenance overhead. Capacitor v6+ packages the exact TypeScript calculation engine into the APK binary (`android/app/src/main/assets/public`), running offline inside Android's native V8 WebView engine with sub-2ms latency.

### Native Hardware Bridge (`ApexHardwarePlugin.java`)
Direct Kotlin/Java integration with Android hardware APIs via `@CapacitorPlugin`:
- **Native Speech Recognition (`SpeechRecognizer`)**:
  - Implements `RecognitionListener` with an intelligent **3000ms end-of-speech silence tolerance** to prevent premature cutoff during tax figure dictation.
  - Returns real-time speech hypotheses to drive the hands-free Senior Tax Reviewer voice agent.
- **Native Text-To-Speech (`TextToSpeech`)**:
  - Hardware-accelerated offline voice synthesis configured with optimal rate (1.02x) and pitch for clear statutory briefing.

### Compiled Binary Details
- **Target OS**: Android 14 (API Level 34)
- **Minimum OS**: Android 7.0 (API Level 24)
- **Architecture**: ARM64 / x86_64
- **Binary Output**: `android/app/build/outputs/apk/debug/app-debug.apk` (~8.8 MB)

---

## 🗂️ Project Repository Structure

```
apextax-compliance-engine/
├── Apex Tax Practice Hub/               # Web Workstation & Core Application
│   ├── return_1040.html                 # 1040 Workstation, Lead Sheets & Statutory Engine
│   ├── returns.html                     # Multi-Entity Practice Hub & Scenario Router
│   ├── sample_slips/                    # Pre-generated Multi-Page Practice PDF Binders
│   │   ├── Alex_Taylor_Master_Slips_TY2025.pdf
│   │   ├── Real_Estate_Investor_Slips_TY2025.pdf
│   │   ├── Pass_Through_K1_Package_TY2025.pdf
│   │   └── Small_Business_1099NEC_TY2025.pdf
│   └── forms/                           # Official IRS 1040 PDFs (Dynamic Split-Screen)
├── android/                             # Native Android Studio Project
│   ├── app/
│   │   ├── src/main/java/com/apextax/practicehub/
│   │   │   ├── MainActivity.java        # Android Entrypoint & Plugin Registration
│   │   │   └── ApexHardwarePlugin.java  # Native Hardware Bridge (STT & TTS)
│   │   └── src/main/assets/public/      # Bundled Web Engine Assets (Offline)
│   ├── build.gradle                     # Top-level Gradle configuration
│   └── gradlew                          # Gradle wrapper executable
├── Instructions IRS/                    # Official IRS TY 2025 Instruction Handbooks
├── capacitor.config.json                # Capacitor native shell configuration
├── build_mobile_dist.js                 # Production asset bundler for Android assets
├── TASKS.md                             # Phase-by-phase implementation ledger
└── README.md                            # Architecture & compliance master documentation
```

---

## 🚀 Quickstart & Development

### 1. Run the Desktop Tax Workstation
The workstation runs completely locally with zero external CDN dependencies:
```bash
# Clone the repository
git clone https://github.com/sireesh0204-stack/apextax-compliance-engine.git
cd apextax-compliance-engine

# Open the Practice Hub in any modern browser
# Double-click or serve locally:
npx serve "Apex Tax Practice Hub"
```
Navigate to `http://localhost:3000/returns.html` to launch the multi-entity dashboard.

### 2. Build the Native Android `.apk`
Prerequisites: Microsoft OpenJDK 17 LTS and Android SDK 34 (`platforms;android-34`, `build-tools;34.0.0`).
```bash
# 1. Sync web engine assets into the Android native directory
node build_mobile_dist.js
npx cap copy android

# 2. Build the Debug APK using the Gradle wrapper
cd android
./gradlew assembleDebug

# Output APK:
# android/app/build/outputs/apk/debug/app-debug.apk
```

### 3. Deploy to Connected Android Device via ADB
```bash
# Verify device connection
adb devices

# Install APK to device
adb install -r android/app/build/outputs/apk/debug/app-debug.apk
```

---

## 🌐 The Sireesh Kumar Public Portfolio Ecosystem

ApexTax is part of a deliberate, 3-pillar technical portfolio demonstrating end-to-end mastery across the tax-technology lifecycle:

| Repository | Tech Stack | Core Domain & Focus |
|:---|:---|:---|
| **[`apextax-compliance-engine`](https://github.com/sireesh0204-stack/apextax-compliance-engine)** | TypeScript, HTML5, Android (Capacitor/Java), pdf-lib | **Client Workstation & Mobile OS**: TY 2025 Form 1040 statutory waterfalls, Big 4 workpapers (`WP-1040`), offline PDF stamping, and native Android `.apk`. |
| **[`doc-eval-harness`](https://github.com/sireesh0204-stack/doc-eval-harness)** | Python, MCP, Promptfoo, XSD | **AI Evaluation & Verification Harness**: 3-layer checks (Schema, Instruction, Render) demonstrating that 7 production tax engine bugs pass government XSD schemas. Includes an MCP server for autonomous LLM self-validation. |
| **[`tax-sandbox`](https://github.com/sireesh0204-stack/tax-sandbox)** | Go 1.22+, IRS/FTB Rules | **Backend Production Engine**: High-throughput Go simulation engine reflecting 6 years of production tax code authorship across 27 state tax regimes (Corvee/Instead). |

---

## 👨‍💻 Author & Contact

**Anasuri Sireesh Kumar**  
*Senior Tax Analyst & Tax Form Implementation Engineer*  
Hyderabad, India &bull; [+91 86861 37374](tel:+918686137374) &bull; [Sireesh0204@gmail.com](mailto:Sireesh0204@gmail.com)  
GitHub: [@sireesh0204-stack](https://github.com/sireesh0204-stack) &bull; LinkedIn: [Sireesh Kumar Anasuri](https://www.linkedin.com)

---

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
All IRS tax forms and instructions are public domain US Government materials under Title 17, Section 105 of the United States Code.

