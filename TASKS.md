# ⚡ ApexTax OS — Master Task Checklist & Implementation Roadmap

> **System Overview**: Enterprise-Grade, Modular Tax Compliance Suite modeled after Intuit ProConnect & CCH Axcess.  
> **Architecture**: Entity-Specific Clean Workstations (`return_1040.html`, `return_1065.html`, `return_1120s.html`) &bull; True Cross-Form Interlinking &bull; Standalone Dual-Monitor Document Binder Popout &bull; 50/50 Live Split-Screen Form Preview &bull; Local Qwen 2.5 14B Reviewer &bull; RTX 3080 Obsidian Aurora Theme.  
> 
> *Instructions*: Mark an item as complete with `[x]` once verified. We build form-by-form, test thoroughly, and only advance upon approval!

---

## 📌 Phase 1: Practice Hub (`returns.html`) & Multi-Entity Router (100% Complete)

- [x] **Task 1.1: Verify & Lock Tax Year 2025 Across Entire Practice Hub**
  - [x] **1.1.1**: Header reads: `⚡ ApexTax Practice Hub | 2025 Tax Compliance`
  - [x] **1.1.2**: Top KPI ribbon displays: `TY 2025 Filing Season`
  - [x] **1.1.3**: All table row badges show `TY 2025`
  - [x] **1.1.4**: Default year in `[+ Create Tax Return]` wizard defaults to `2025`
  - [x] **1.1.5**: Storage key updated to purge any stale 2024 cached items from browser memory

- [x] **Task 1.2: Entity-Specific Routing from Practice Hub**
  - [x] Creating/Opening **Form 1040** routes cleanly to `return_1040.html?return={id}`
  - [x] Decouple individual hardcoded client data from the base engine; all new returns boot to a **True Clean Blank $0 Return** with custom taxpayer info from wizard
  - [x] Box 7 Interactive Attached Schedules & Statutory Focus drawer with live search, 25+ IRS forms, and 2025 conditional rules (8995 vs 8995-A exclusivity, Schedule D → Form 8949 auto-link, Schedule C → Schedule SE auto-link)
  - [x] In-flow collapsible container eliminating modal overflow bugs

- [x] **Task 1.3: Delete Return / Archive & Trash Management**
  - [x] Direct table row actions with clean `[Launch Workstation ↗]` and red `[✖]` quick-remove buttons
  - [x] Dedicated `#quickRemoveModal` for choosing `📁 Archive Return` vs `🗑️ Move to Trash`
  - [x] Dedicated tab pill: `Archived / Trash (Count)` in entity filter bar
  - [x] In Trash view, rows display `[Restore Return ↩]` and `[Delete Permanently ✖]`
  - [x] `[↺ Reset Default Returns]` button to safely restore curriculum cases

---

## 🏛️ Phase 2: Form-by-Form True Interlinked Workstation Architecture (`return_1040.html`) (100% Complete)

- [x] **Task 2.1: Blank Form 1040 Base Shell & Collapsible Form Navigation Tree**
  - [x] Clean Form 1040 (Lines 1 to 38) starting at **$0.00**
  - [x] Left Navigation Tree listing all standard supporting forms & schedules (12 Forms):
    - Main: `Form 1040`
    - Income/Loss: `Schedule 1` (Additional Income & Adjustments)
    - Itemized/Standard: `Schedule A` (Itemized Deductions & SALT cap)
    - Interest & Divs: `Schedule B` (Interest & Ordinary Dividends)
    - Business: `Schedule C` (Sole Proprietorship P&L)
    - Capital Gains: `Schedule D` & `Form 8949` (Capital Assets & Crypto)
    - Supplemental Income: `Schedule E` (Rental, Real Estate Syndication, Partnerships & S-Corps)
    - Self-Employment: `Schedule SE` (Self-Employment Tax)
    - Limitations & AMT: `Form 8582` (Passive Activity Losses), `Form 6251` (AMT), `Form 8995-A` (QBI §199A), `Form 8960` (NIIT)
  - [x] **ProConnect View Toggle**: `[Show All Forms (12)]` vs `[Show Active/Edited Forms Only (N)]`
  - [x] **Collapsible Left Sidebar**: `[◀]` button collapses tree into a **56px slim icon rail** (`#leftSidebarSlimRail`)

- [x] **Task 2.2: True Statutory Cross-Form Interlinking Engine + 4 Official TY 2025 IRS Worksheets**
  - [x] Schedule C Line 31 (Net Profit) &rarr; Flows automatically into Schedule 1 Line 3 & Schedule SE
  - [x] Schedule SE Line 12 &rarr; Flows to Schedule 2 Line 4 &rarr; Form 1040 Line 17
  - [x] Schedule SE Line 13 &rarr; Flows to Schedule 1 Line 15 (50% SE Tax Deduction) &rarr; Form 1040 Line 10 (AGI Calculation)
  - [x] Schedule 1 Line 10 (Total Additional Income) &rarr; Flows into Form 1040 Line 8
  - [x] Schedule 1 Line 26 (Total Adjustments to Income) &rarr; Flows into Form 1040 Line 10 (AGI Calculation)
  - [x] Schedule D Line 16 &rarr; Flows into Form 1040 Line 7
  - [x] **Worksheet #1**: Form 1040 Line 16 Qualified Dividends & Net Capital Gain 25-Line Tax Worksheet (0%, 15%, 20% statutory preferential brackets)
  - [x] **Worksheet #2**: Schedule A Line 5e SALT Phaseout Worksheet ($40,000 base cap, 30% reduction over $500k AGI, $10,000 statutory floor) vs Standard Deduction
  - [x] **Worksheet #3**: Form 8995-A SSTB §199A Reduction Engine ($197.3k/$394.6k thresholds, $50k/$100k phaseout, $0 cutoff) &rarr; Form 1040 Line 13a
  - [x] **Worksheet #4**: Form 6251 Line 5 AMT Exemption Phaseout Engine ($88.1k/$137k base, 25% phaseout over $626.35k/$1.252m AMTI) &rarr; Schedule 2 Line 1 &rarr; Form 1040 Line 17
  - [x] Form 8960 Net Investment Income Tax (3.8% surtax on lesser of NII or MAGI excess) &rarr; Schedule 2 Line 12 &rarr; Form 1040 Line 17

- [x] **Task 2.3: Standalone Popout Source Document Binder & Dual-Monitor Detach**
  - [x] Standalone `#sourceDocumentPopoutModal` with `[📂 Popout Source Documents ↗]` in top navbar
  - [x] **Dual-Monitor Detach**: `[⧉ Detach Browser Popup]` opens independent `1180x860` window via `window.open`
  - [x] Dynamic source slips for active returns:
    - `W-2` (Wages, Fed Tax, Social Security/Medicare)
    - `1099-INT` / `1099-DIV` (Ordinary & Qualified Dividends)
    - `1099-NEC` (Nonemployee Compensation)
    - `1099-B` (Covered/Noncovered Capital Gain Sales)
    - `Form 3921` (Exercise of Incentive Stock Options — ISO AMT Bargain Element)
    - `Schedule K-1` (Pass-Through Allocations)
  - [x] Clean Drag & Drop Slip Uploader empty-state when return is blank or cleared to `$0`
  - [x] 2-Way Slip Lineage: Clicking any box amount or `[Jump & Transfer ↗]` keys value into target form line with **1.2-second emerald pulse animation**

- [x] **Task 2.4: 50/50 Split-Screen Multi-Form Official IRS PDF Viewer & NotebookLM Line-by-Line Stamping**
  - [x] Top navbar `[◫ Split Form Preview]` button toggling dynamic 50/50 split workspace
  - [x] **Dynamic Form PDF Switching (All 12 IRS Forms)**: Switching forms in left navigation tree immediately updates the split pane to the corresponding official IRS PDF in `forms/` (`f1040.pdf`, `f1040s1.pdf`, `f1040s2.pdf`, `f1040sa.pdf`, `f1040sb.pdf`, `f1040sc.pdf`, `f1040sd.pdf`, `f1040se.pdf`, `f1040sse.pdf`, `f8995a.pdf`, `f6251.pdf`, `f8960.pdf`)
  - [x] **Dual-Mode Viewer**: Instant toggle between `[📄 Official PDF]` (embedded high-fidelity iframe) and `[📊 Values Table]` (NotebookLM statutory line mapping summary)
  - [x] **Dual-Monitor Popout**: `[⧉ Popout PDF]` opens active IRS PDF in an independent detached browser window
  - [x] **NotebookLM Ground-Truth Line Mappings**: Real-time reactive data population for Form 1040, Schedule A, Schedule C, Schedule D, Schedule SE, Schedule 1, Schedule 2, Form 8995-A, Form 6251, and Form 8960
  - [x] Clickable line rows in the values table jump and focus directly to the corresponding input field on the workpaper canvas

- [x] **Task 2.5: Senior Tax Reviewer AI (Local Qwen 2.5 14B) & Panel Minimize**
  - [x] Reviewer timeout extended to **30,000ms (30s)** for local RTX 3080 Ollama inference
  - [x] Collapsible right pane: `[▶]` button collapses into slim vertical badge strip (`#rightReviewerSlimStrip`) displaying `AI REVIEWER • 5/5 PASS`
  - [x] Pinned chat conversation stream and interactive diagnostic audit tray

---

## 🏛️ Phase 2.6: Big 4 Workpaper Engine, Dynamic Schedule Derivation & Practice Slips Hub (Completed: 2026-10-21 15:38 IST)

- [x] **Task 2.6.1: Standalone Practice Slips Hub on Dashboard (`returns.html`)** *(Completed: 2026-10-21 14:55 IST)*
  - [x] Offline multi-page PDF generation via `pdf-lib.min.js` without internet or external CDN dependencies.
  - [x] 1040 Persona Scenarios: Real Estate, Small Business, Pass-Through K-1, Portfolio, W-2 Tech, and Complete Binder.
  - [x] Realistic randomized figures generation with audit discrepancy simulation toggle.
  - [x] Strict practice isolation: PDF downloads directly to local drive without auto-injecting data into returns.

- [x] **Task 2.6.2: Entity-Driven Dynamic Scenarios in Create Return Modal (`returns.html`)** *(Completed: 2026-10-21 15:38 IST)*
  - [x] Overhauled Section 7: Completely removed static manual schedules checklist.
  - [x] Entity-Specific Dynamic Scenarios: Form 1040 (Alex Taylor Master, Real Estate, Small Business, K-1s, Portfolio, Blank), Form 1065, Form 1120-S, Form 1120.
  - [x] Direct inline `[📥 Download Practice Slips PDF]` button and audit discrepancy simulation toggle right inside the engagement creation wizard.

- [x] **Task 2.6.3: Selective Slip Upload & 4-Point Audit Verification Engine (`return_1040.html`)** *(Completed: 2026-10-21 15:00 IST)*
  - [x] Decoupled automatic slip injection; returns boot to clean $0.00 canvas.
  - [x] Selective extraction: Only flows data for the specific files uploaded by the preparer.
  - [x] Visual verification badging: Green `[✓ Verified Source Document]` for clean slips, red `[❗ Discrepancy Flag]` with interactive hover tooltip card for audit traps.

- [x] **Task 2.6.4: Big 4 / Top 10 Accounting Workpaper Indexing & Statutory Tickmarks (`return_1040.html`)** *(Completed: 2026-10-21 15:00 IST)*
  - [x] Standard workpaper lead sheet banners: `WP-1040-E` (IRC §61(a)(5), §469, §168(c) MACRS 27.5-Yr), `WP-1040-C` (IRC §162(a), §274(n), §1402 SE Tax), `WP-1040-A` (IRC §164 SALT, §163(h) Mortgage, §213 7.5% AGI).
  - [x] Statutory tickmarks: `[✓ Agrees to W-2]` (Line 1a), `[✓ Tied to Sch 1 & SE]` (Line 31), `[✓ Tied to 8582]` (Line 22).

- [x] **Task 2.6.5: Dynamic Workpaper Schedule Reveal (`return_1040.html`)** *(Completed: 2026-10-21 15:38 IST)*
  - [x] Supporting schedule workpapers (Schedule C, Schedule E, Schedule A, Schedule B, Schedule D, Schedule SE, Form 8582, Form 8995-A) reveal dynamically based on the uploaded source slips.
  - [x] Clean empty state displays only Form 1040 Core; uploading slips unhides their corresponding schedules.

- [x] **Task 2.6.6: Ground-Truth NotebookLM Statutory Rules Integration** *(Completed: 2026-10-21 15:38 IST)*
  - [x] IRC §163(h) $750k acquisition indebtedness ratio check on Form 1098.
  - [x] IRC §469 $25k Active Participation PAL allowance & $100k–$150k MAGI phaseout formula on Schedule E / Form 8582.
  - [x] Schedule SE net earnings ($0.9235 \times \text{Net Profit}$) and 50% above-the-line deduction to Schedule 1 Line 15.
  - [x] Form 8995 QBI base formula (Sch C Net Profit minus Deductible SE Tax).
  - [x] Form 7203 S-Corp basis ordering rule (beginning basis minus distributions = allowed loss cap).

- [x] **Task 2.6.7: Senior Reviewer Ground-Truth Engine & NotebookLM Dual-Monitor Copilot (`return_1040.html`)** *(Completed: 2026-10-21 16:05 IST)*
  - [x] **Dual-Monitor NotebookLM Copilot Launch Button**: `[📚 NotebookLM ↗]` in reviewer header launches authenticated NotebookLM session (`authuser=1`) in a dedicated 1200x900 sidecar popup window.
  - [x] **Live Context Transmitter**: `[📋 Copy Question with Live Return Context]` bundles active engagement taxpayer details, Form 1040 lines (1a through 24), supporting schedules (C, E, SE, A, 6251, 8960), and question into clipboard for instant paste into NotebookLM.
  - [x] **Instant Deterministic Statutory Assistant (0ms latency)**: Covers 6 deep statutory domains:
    1. Pass-Through Partner / Shareholder (IRC §702, §1402(a)(1) SE Tax vs S-Corp Rev. Rul. 59-221, §1366(d) / §1367 Form 7203 Basis, §199A QBID).
    2. Rental Real Estate & PAL (IRC §469(i) $25k active participation, $100k-$150k MAGI phaseout, Form 8582 suspended loss carryforwards).
    3. Schedule C & SE Tax (IRC §162, §1401, §1402(a)(12) 0.9235 factor, 50% above-the-line deduction to Sch 1 Line 15, Treas. Reg. §1.199A-3 QBI base reduction).
    4. Mortgage Indebtedness & Form 1098 (IRC §163(h)(3) $750k acquisition cap, Pub 936 ratio check, Schedule A Line 8a vs Schedule E Line 12 tracing).
    5. Portfolio, Capital Gains & Dividends (IRC §6049 $1,500 Schedule B threshold, §1(h) preferential rates, §1211 $3k loss limit, §1411 NIIT).
    6. Alternative Minimum Tax & ISOs (IRC §55, §56, §421/§422 bargain element on Form 6251 Line 2i, exemption phaseout, Form 8801 MTC).
  - [x] **Non-Blocking Ollama Integration**: 800ms readiness ping to `/api/tags` avoids 2.5s-30s browser freezes when local LLM is offline, automatically serving comprehensive ground-truth audit cards.

- [x] **Task 2.6.8: Practice Slips Streamlining, Local `sample_slips/` Hub & Workstation Quick-Loader** *(Completed: 2026-10-21 16:16 IST)*
  - [x] **Purged Header Redundancy (`returns.html`)**: Removed redundant `[🎲 Practice Slips Hub]` button and duplicate standalone modal from dashboard header, consolidating all scenario slip downloads strictly into Section 7 of `#createReturnModal`.
  - [x] **Native Directory Picker (`window.showSaveFilePicker`)**: Updated `downloadWizardPracticeSlipsPdf()` to prompt the native Windows Save dialog pre-populated with filename so the preparer can save directly into `sample_slips/`.
  - [x] **Pre-Populated Project `sample_slips/` Repository**: Pre-generated authentic multi-page PDFs for all scenarios directly on disk (`Alex_Taylor_Master_Slips_TY2025.pdf`, `Real_Estate_Investor_Slips_TY2025.pdf`, `Small_Business_1099NEC_TY2025.pdf`, `Pass_Through_K1_Package_TY2025.pdf`, `Portfolio_1099B_INT_DIV_TY2025.pdf`, `Complete_Practice_Binder_TY2025.pdf`).
  - [x] **Workstation Empty-State Quick-Loader (`return_1040.html`)**: Added one-click quick-load chips in the slip uploader dropzone, allowing instant loading of any practice scenario directly from `sample_slips/` without manually browsing files.

---

## 🎨 Phase 3: Ultra-Premium UI/UX (RTX 3080 3D Depth & Fluid Motion)

- [x] **Task 3.1: Tactile 3D Buttons & Dynamic Depth Shading**
  - [x] Primary buttons (`[+ Create Tax Return]`, `[Launch Workstation ↗]`, `[⚡ Audit & Verify]`) styled with tactile bevels, top specular highlights, and active depression
  - [x] Glass-panel cards with responsive hover lifts and status glow flares (Emerald for compliant/active, Rose for delete/critical, Sky for popouts)
- [x] **Task 3.2: Silky Fluid Animations & Transitions**
  - [x] Collapsible left and right panels with 300ms smooth width transitions
  - [x] 1.2-second glowing pulse animation for field drill-down navigation
  - [x] Modals enter with backdrop blur and smooth fade/scale

---

## 📱 Phase 3.5: Native Android Mobile APK Toolchain & Hardware Bridges (Completed: 2026-10-22 01:03 IST)

- [x] **Task 3.5.1: Microsoft OpenJDK 17 LTS & Android SDK 34 Platform Setup** *(Completed: 2026-10-22 00:58 IST)*
  - [x] Installed `Microsoft.OpenJDK.17` (`v17.0.20.1`) on Windows host machine.
  - [x] Installed Android SDK Command-line Tools, pre-configured license hashes, and downloaded `platforms;android-34`, `build-tools;34.0.0`, and `platform-tools` (`adb`) in `d:\Android\Sdk`.
  - [x] Configured `local.properties` with `sdk.dir=D\:\\Android\\Sdk`.

- [x] **Task 3.5.2: Capacitor v6+ Hybrid Native Shell & Asset Pipeline** *(Completed: 2026-10-22 00:56 IST)*
  - [x] Created `package.json` with `@capacitor/core`, `@capacitor/cli`, `@capacitor/android`, `@capacitor/camera`, `@capacitor/filesystem`, `@capacitor/share`, `@capacitor/preferences`.
  - [x] Automated mobile build staging script `build_mobile_dist.js` assembling `dist/` with `index.html`, `returns.html`, `return_1040.html`, official IRS PDFs in `forms/`, sample slip packages in `sample_slips/`, and offline `pdf-lib`.
  - [x] Scaffolded `android/` platform project via `npx cap add android`, synchronizing all assets into `android/app/src/main/assets/public/`.

- [x] **Task 3.5.3: Native Android Hardware Bridge & Manifest Architecture** *(Completed: 2026-10-22 00:59 IST)*
  - [x] Created `ApexHardwarePlugin.java` binding native Android `SpeechRecognizer` with statutory 3000ms silence tolerance (`EXTRA_SPEECH_INPUT_COMPLETE_SILENCE_LENGTH_MILLIS`) and native `TextToSpeech` with pitch/speech rate tuning.
  - [x] Registered `ApexHardwarePlugin` inside `MainActivity.java`.
  - [x] Configured `AndroidManifest.xml` with Camera, Audio, Storage permissions, FileProvider for PDF sharing, and Android 11+ `<queries>` intents for speech services.

- [x] **Task 3.5.4: Successful Production-Grade APK Compilation** *(Completed: 2026-10-22 01:03 IST)*
  - [x] Executed Gradle 8.2.1 daemon (`.\gradlew.bat assembleDebug`).
  - [x] **186 actionable tasks executed successfully in 1m 13s**.
  - [x] Output verified: `d:\Tax Compliance Preparation\android\app\build\outputs\apk\debug\app-debug.apk` (8.86 MB).

---

- [ ] **Task 4.1: Voice-Driven Interactive Interview Room**
  - [ ] Top nav button: `[🎙️ Technical Mock Interview]` launches the Interview Arena
  - [ ] **Spoken Question Delivery (Browser TTS)**:
    - Virtual Senior Manager / Partner asks technical tax questions out loud with speech synthesis
    - Visual speaking wave visualizer indicates AI is currently speaking
  - [ ] **Speech-to-Text Input (Browser STT / Web Speech API)**:
    - User presses mic (or holds spacebar/hotkey) and speaks their technical answer
    - Live transcription displays in real-time with waveform indicator
  - [ ] **Text Fallback**:
    - Optional keyboard input box for typing answers if working silently

- [ ] **Task 4.2: Local Qwen 14B Statutory Defense Scoring & Follow-Ups**
  - [ ] Qwen 14B analyzes spoken response across 3 dimensions:
    1. *Statutory Accuracy & IRC Code Citations* (§469, §199A, §704(b), §1368, etc.)
    2. *Audit Defense & Risk Identification*
    3. *Executive Communication & Professional Demeanor*
  - [ ] AI delivers immediate constructive feedback, score (1–10), and asks an adaptive follow-up question
  - [ ] Includes direct sync link to your NotebookLM: `https://notebook.google.com/notebook/7f8a6c49-fbdb-4404-bd17-5512c528da00?authuser=1`

- [ ] **Task 4.3: Interactive Web Context & Line-Level Attachment Engine for Qwen 14B**
  - [ ] **Click-to-Attach**: Clicking an "Ask AI" pill on any line card attaches that line's full statutory payload as an active context chip in the chat box
  - [ ] **Hover Tooltip & Hotkey (`Alt + R`)**: Hovering any field shows an interactive mini tooltip with IRC rule, and pressing `Alt + R` automatically sends that line context to Qwen 14B
  - [ ] **Drag-and-Drop Form Line onto Chat**: Dragging any line card or document slip and dropping it into the chat pane attaches it as a contextual reference
  - [ ] **Live Full-Return Snapshot**: Chat payload automatically injects active return state (AGI, Taxable Income, active diagnostic flags)

---

## ⚡ Phase 5: Partnership (1065) & S-Corp (1120-S) Workstations

- [ ] **Task 5.1: Build `return_1065.html`**
  - [ ] Form 1065 Page 1 (Ordinary Business Income)
  - [ ] Schedule K (Partners' Distributive Share Items)
  - [ ] Schedule K-1 Generator for Partner Allocations (§704(b) capital accounts, recourse/nonrecourse liabilities)
  - [ ] Schedule M-1 (Book-to-Tax Reconciliation) & Schedule M-2 (Analysis of Partners' Capital Accounts)

- [ ] **Task 5.2: Build `return_1120s.html`**
  - [ ] Form 1120-S Page 1 (Corporate Income & Expenses)
  - [ ] Form 1125-A (Cost of Goods Sold) & Form 1125-E (Compensation of Officers)
  - [ ] Schedule M-1 & Schedule M-2 (AAA, OAA, and Retained Earnings Tracking)
  - [ ] Form 7203 (S-Corporation Shareholder Stock and Debt Basis Limitations)

---

## 🚀 Phase 6: Career Launch & Productivity/Health Tools

- [ ] **Task 6.1: High-Impact LinkedIn Post & Demo Video Showcase**
  - [ ] Hook & Story Script: "How I Built an Enterprise-Grade Virtual Tax Software for ₹0 After Getting Laid Off"
  - [ ] Screen Recording storyboard & showcase clips (Obsidian Aurora theme, RTX 3080 telemetry, 1040/1065/1120-S flows, NotebookLM integration)
  - [ ] Architecture diagram & technical callouts (Antigravity + NotebookLM Ground-Truth + Argon 4 + Local Qwen 14B)

- [ ] **Task 6.2: Deep-Focus & Daily Health Productivity Companion (Web/PWA & Mobile Push)**
  - [ ] Pomodoro / Study Focus Timer tuned for deep tax return preparation
  - [ ] Mobile push reminders for study sessions via Web Push API / Telegram / Discord Webhook
  - [ ] Hydration & Ergonomic Break Reminders ("Drink water", "20-20-20 eye relief", "Stretch breaks")
  - [ ] End-of-day auto-sync to `DAILY_LEARNING_LOG.md` and GitHub
