# Daily Tax Compliance & Engineering Learning Log

> **Owner**: Anasuri Sireesh Kumar  
> **Track**: High-Net-Worth Individual (1040), Partnership / Real Estate (1065), S-Corporation (1120-S) & Tax Technology Engineering  
> **Repository Ground Truth**: Permanent log of hands-on return preparation, technical tax reconciliations, and Enterprise & National Firm interview drill mastery.

---

## Log Entries

### Day 00: Foundation Architecture & Setup (October 14–15, 2026)
* **Milestone**: Ecosystem Setup, Spatial UI Curriculum Tracker & Real Estate Industry Alignment
* **Key Achievements**:
  - Established 5-entity collaboration pipeline: NotebookLM (Tax Data Extractor) $\rightarrow$ Antigravity (Architect & Prompt Engineer) $\rightarrow$ Argon 4 (Code Generator) $\rightarrow$ Sireesh (Lead Preparer) $\leftrightarrow$ Local Qwen 14B (Senior Reviewer).
  - Built and deployed `curriculum.html` with VisionOS Spatial UI and live background sync (`sync_server.py`) linked directly to `CURRICULUM_TRACKER.md`.
  - Analyzed and decoded public accounting Real Estate tax opportunities (Forms 1065/1120-S, Form 8825, Form 4562, §465(b)(6) Qualified Nonrecourse Financing, §469(i) Rental Allowance, §469(c)(7) REPS).
  - Created master career context record (`CAREER_AND_PROJECT_CONTEXT.md`).
* **Technical Takeaway**: In accounting firms, "Real Estate" implies Form 8825 flow-through to Schedule K Line 2, cost segregation on Form 4562 (27.5-yr vs 39-yr MACRS), and debt characterization under §752 for at-risk basis under §465(b)(6).
* **Next Target**: Day 01 — Form 1040 Statutory Workstation, Practice Hub Multi-Entity Router, and 12-Form Cross-Tie Engine.

---

### Day 01: Form 1040 Statutory Workstation, 4 IRS Worksheets & Dual-Monitor Binder (October 15, 2026)
* **Date**: October 15, 2026
* **Return Prepared**: Alex Morgan (Tech Lead HNI: W-2, §56(b)(3) ISO Form 3921, 1099-NEC, 1099-B, Sch C/SE, AMT) & Dr. Marcus Vance (Physician: W-2, SSTB 1099-NEC, K-1, Sch A SALT, §199A QBID)
* **Forms & Schedules Reconciled**: Form 1040 Lines 1a through 37; Schedules 1, 2, A, B, C, D, E, SE, and Forms 8995-A, 6251, 8960
* **Statutory Engines Implemented**:
  1. *Form 1040 Line 16 Preferential Rates Worksheet (25-Line Engine)*: Figuring ordinary tax on Line 5, applying 0%/15%/20% preferential capital gain/dividend tiers, and entering $\min(\text{L23}, \text{L24})$.
  2. *Schedule A Line 5e SALT Phaseout Worksheet*: $40,000 base cap ($20,000 MFS), reduced by 30% of AGI excess over $500,000, subject to $10,000 statutory floor ($5,000 MFS).
  3. *Form 8995-A SSTB §199A Reduction Engine*: $197,300 ($394,600 MFJ) threshold, $50,000 phaseout range, and $0 cutoff above $247,300 ($494,600 MFJ).
  4. *Form 6251 Line 5 AMT Exemption Phaseout Engine*: $88,100 base exemption ($137,000 MFJ), reduced by 25% of AMTI excess over $626,350 ($1,252,700 MFJ).
* **Architectural Breakthroughs**:
  - *Dual-Monitor Standalone Popout Binder*: Dedicated `#sourceDocumentPopoutModal` with `window.open` detached browser popup passing values back via `window.opener.transferSlipValueFromPopup` with a 1.2s emerald glow pulse.
  - *50/50 Split-Screen Form Preview*: Live IRS Form 1040 paper sheet replica updating reactively with clickable line drill-downs.
  - *Practice Hub Router (`returns.html`)*: Interactive 2025 IRS attached schedules drawer with live search and conditional rules.
  - *Full Brand Sanitization*: Completely sanitized all "Big 4" references to "Enterprise & National Firm Standards" and "Senior Tax Compliance Reviewer" to appeal across Top 10 public accounting and corporate tax tech firms.
* **Senior Technical Interview Question Drilled**: "Explain why an ISO exercise generates no regular tax on Form 1040 Line 1a, but triggers Form 6251 Line 2i alternative minimum tax, and how that affects the AMT exemption phaseout under §55(d)."
* **Confidence Level**: [x] Competent  [x] Interview Ready

---

### Day 02: Big 4 Workpaper Engine, Dynamic Schedule Derivation & Dual-Monitor NotebookLM Copilot (October 21, 2026)
* **Date**: October 21, 2026
* **Milestone**: Senior Tax Reviewer Ground-Truth Engine, Entity-Driven Dynamic Scenarios, Offline PDF Generation & Dual-Monitor NotebookLM Integration
* **Key Achievements**:
  1. *Dual-Monitor NotebookLM Copilot & Live Context Transmitter*:
     - Integrated `[📚 NotebookLM ↗]` sidecar launcher in `return_1040.html` header opening the authenticated workspace (`authuser=1`) in a dedicated 1200x900 window.
     - Built `[📋 Copy Question with Live Return Context]` transmitter bundling active return figures (Form 1040 Lines 1a–24, Schedules C, E, SE, A, Forms 6251, 8960, and active audit flags) directly into clipboard for one-click pasting (`Ctrl+V`) into NotebookLM.
  2. *Instant Ground-Truth Statutory Engine (0ms Latency)*:
     - Replaced unreliable local LLM hallucinations on pass-through income with deterministic statutory intelligence across 6 core domains:
       - **Pass-Through Entities (K-1s)**: IRC §702, §1402(a)(1) general vs limited partner SE tax, S-Corp Box 1 ordinary income exemption (*Rev. Rul. 59-221*), and Form 7203 basis ordering rules (§1366(d) / §1367).
       - **Rental Real Estate & PAL**: IRC §469(i) $25,000 active participation allowance, $100k–$150k MAGI 50% phaseout, and Form 8582 suspended loss carryforwards (§469(b)).
       - **Schedule C & SE Tax**: IRC §162 ordinary/necessary deductions, Schedule SE 0.9235 statutory multiplier (§1402(a)(12)), 50% above-the-line deduction to Schedule 1 Line 15 (§164(f)), and Treas. Reg. §1.199A-3 QBI base reduction.
       - **Mortgage Indebtedness & Form 1098**: IRC §163(h)(3) $750,000 acquisition debt ceiling, IRS Pub 936 ratio formula, and Schedule A Line 8a vs Schedule E Line 12 tracing.
       - **Portfolio & Capital Gains**: IRC §6049/§6042 $1,500 Schedule B threshold, IRC §1(h) preferential capital gains/qualified dividend rates, and IRC §1411 3.8% NIIT.
       - **AMT & Stock Options**: IRC §55/§56, Form 6251 Line 2i ISO spread addback, and Form 8801 Minimum Tax Credit.
     - Added 800ms readiness ping to Ollama `/api/tags` to avoid browser freezes when local AI is offline.
  3. *Practice Slips Hub Architecture & Project `sample_slips/` Integration*:
     - Consolidated all practice persona scenarios into Section 7 of `#createReturnModal` in `returns.html`, removing redundant dashboard header buttons.
     - Implemented `window.showSaveFilePicker` allowing direct saving into project folders.
     - Pre-generated authentic multi-page PDFs for all scenarios directly into `Apex Tax Practice Hub/sample_slips/` (`Alex_Taylor_Master_Slips_TY2025.pdf`, `Real_Estate_Investor_Slips_TY2025.pdf`, `Small_Business_1099NEC_TY2025.pdf`, `Pass_Through_K1_Package_TY2025.pdf`, `Portfolio_1099B_INT_DIV_TY2025.pdf`, `Complete_Practice_Binder_TY2025.pdf`).
     - Added one-click quick-load chips in the `return_1040.html` dropzone to load any practice package instantly without opening file dialogs.
  4. *Big 4 Lead Sheets & Dynamic Schedule Unhiding*:
     - Added accounting lead sheets `WP-1040-E`, `WP-1040-C`, `WP-1040-A` with statutory tickmarks (`[✓ Agrees to W-2]`, `[✓ Tied to Sch 1 & SE]`, `[✓ Tied to 8582]`).
     - Supporting schedules now remain hidden on a clean $0.00 return and dynamically reveal only when their triggering source documents are uploaded.
* **Technical Takeaways**:
  - Web browser sandboxing prevents silent writes to arbitrary local paths, making the combination of pre-populated project `sample_slips/`, `window.showSaveFilePicker`, and in-workstation quick-load chips the gold standard UX for local tax preparation tools.
  - S-Corp distributions must be deducted from basis *before* losses are absorbed (IRC §1367(a)(2)(A)), preventing shareholders from artificially taking losses against distributed equity.
* **Confidence Level**: [x] Competent  [x] Interview Ready

---

### Day 02.5: Native Android Mobile APK Toolchain & Hardware Bridges (October 22, 2026)
* **Date**: October 22, 2026
* **Milestone**: Native Android `.apk` Toolchain Assembly, Capacitor v6+ Shell, and Native Hardware Bridge Integration
* **Key Achievements**:
  1. *Toolchain Provisioning*:
     - Installed Microsoft OpenJDK 17 LTS (`v17.0.20.1`) on Windows.
     - Installed Android Command-Line Tools and provisioned official Google Android SDK 34 (`platforms;android-34`, `build-tools;34.0.0`, and `platform-tools` including `adb.exe`) into `d:\Android\Sdk`.
     - Pre-configured Google SDK license agreements in `d:\Android\Sdk\licenses\android-sdk-license`.
  2. *Capacitor v6+ Hybrid Native Shell*:
     - Initialized project `package.json` with Capacitor v6 core, camera, filesystem, preferences, and share plugins.
     - Created `build_mobile_dist.js` staging all web assets (`index.html`, `returns.html`, `return_1040.html`), all 12 official IRS PDFs in `forms/`, all practice slip sets in `sample_slips/`, and `pdf-lib` into `dist/`.
     - Generated native Android project (`android/`) with assets synchronized directly into `android/app/src/main/assets/public/`.
  3. *Native Android Hardware Plugin (`ApexHardwarePlugin.java`)*:
     - Built custom native bridge exposing Android's `SpeechRecognizer` with statutory 3000ms silence tolerance (`EXTRA_SPEECH_INPUT_COMPLETE_SILENCE_LENGTH_MILLIS`) and `TextToSpeech` with rate/pitch tuning for the Senior Mock Interview Arena.
     - Registered plugin in `MainActivity.java` and configured `AndroidManifest.xml` with Camera, Audio, Storage permissions, and FileProvider for PDF viewing.
  4. *Successful Android `.apk` Compilation*:
     - Executed Gradle 8.2.1 daemon (`.\gradlew.bat assembleDebug`).
     - **Result: 186 actionable tasks executed successfully in 1m 13s**.
     - Compiled binary artifact generated: `d:\Tax Compliance Preparation\android\app\build\outputs\apk\debug\app-debug.apk` (8.86 MB).
* **Technical Takeaway**:
  - Combining a deterministic, zero-CDN web compliance engine with a Capacitor Android native shell eliminates cross-language calculation drift, guarantees 100% vector PDF stamping parity via `pdf-lib`, and unlocks native OS hardware capabilities without having to rewrite thousands of lines of tax logic into Kotlin or Dart.
* **Confidence Level**: [x] Competent  [x] Interview Ready

---

### Day 03: [Upcoming] Form 1065 Partnership Workstation & Real Estate Syndication (Form 8825 / Schedule K-1)
* **Date**: [Upcoming Next Session]
* **Target Return**: Real Estate Holding Partnership (Form 1065 Page 1, Form 8825, Schedule K, Partner Allocations on Schedule K-1)
* **Forms & Schedules to Reconcile**: Form 1065 Lines 1–22, Form 8825 Lines 1–21, Schedule K Lines 1–20c, Schedule K-1 (Items J, K, L, M), Schedule M-1 Book-to-Tax Reconciliations
* **Key Drills**: §704(b) capital accounts, §465(b)(6) Qualified Nonrecourse Financing debt allocations, and §469 passive loss grouping.
* **Confidence Level**: [ ] Needs Review  [ ] Competent  [ ] Interview Ready

---

*(Additional daily entry templates are auto-populated as each module is executed)*
