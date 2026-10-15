# ⚡ ApexTax OS — Master Task Checklist & Implementation Roadmap

> **System Overview**: Enterprise-Grade, Modular Tax Compliance Suite modeled after Intuit ProConnect & CCH Axcess.
> **Architecture**: Entity-Specific Clean Workstations (`return_1040.html`, `return_1065.html`, `return_1120s.html`) &bull; True Cross-Form Interlinking &bull; Source Document Auto-Ingestion &bull; Local Qwen 2.5 14B Reviewer &bull; RTX 3080 Obsidian Aurora Theme.
> 
> *Instructions*: Mark an item as complete with `[x]` once verified. We build form-by-form, test thoroughly, and only advance upon approval!

---

## 📌 Phase 1: Practice Hub (`returns.html`) & Multi-Entity Router

- [x] **Task 1.1: Verify & Lock Tax Year 2025 Across Entire Practice Hub**
  - [x] **1.1.1**: Header reads: `⚡ ApexTax Practice Hub | 2025 Tax Compliance`
  - [x] **1.1.2**: Top KPI ribbon displays: `TY 2025 Filing Season`
  - [x] **1.1.3**: All table row badges show `TY 2025`
  - [x] **1.1.4**: Default year in `[+ Create Tax Return]` wizard defaults to `2025`
  - [x] **1.1.5**: Storage key updated to purge any stale 2024 cached items from browser memory

- [ ] **Task 1.2: Entity-Specific Routing from Practice Hub**
  - [ ] Creating/Opening **Form 1040** routes cleanly to `return_1040.html?return={id}`
  - [ ] Creating/Opening **Form 1065** routes cleanly to `return_1065.html?return={id}`
  - [ ] Creating/Opening **Form 1120-S** routes cleanly to `return_1120s.html?return={id}`
  - [ ] Decouple individual hardcoded client data (Marcus Vance) from the base engine; all new returns boot to a **True Clean Blank $0 Return** with custom taxpayer info from wizard

- [ ] **Task 1.3: Delete Return / Archive & Trash Management**
  - [ ] Each table row has an action dropdown `[...]` with `📁 Archive Return` and `🗑️ Move to Trash`
  - [ ] Dedicated tab pill: `Archived / Trash (Count)` in entity filter bar
  - [ ] In Trash view, rows display `[Restore ↩]` and `[Permanently Delete ✖]`
  - [ ] Toast notification with `[Undo ↩]` on delete/archive
  - [ ] `[↺ Reset Master Cases]` button to safely restore default curriculum cases

---

## 🏛️ Phase 2: Form-by-Form True Interlinked Workstation Architecture (`return_1040.html`)

- [ ] **Task 2.1: Blank Form 1040 Base Shell & Form Navigation Tree**
  - [ ] Clean Form 1040 (Lines 1 to 38) starting at **$0.00**
  - [ ] Left Navigation Tree listing all standard supporting forms & schedules:
    - Main: `Form 1040`
    - Income/Loss: `Schedule 1` (Additional Income & Adjustments)
    - Itemized/Standard: `Schedule A` (Itemized Deductions & SALT cap)
    - Interest & Divs: `Schedule B` (Interest & Ordinary Dividends)
    - Business: `Schedule C` (Sole Proprietorship P&L)
    - Capital Gains: `Schedule D` & `Form 8949` (Capital Assets & Crypto)
    - Supplemental Income: `Schedule E` (Rental, Real Estate Syndication, Partnerships & S-Corps)
    - Self-Employment: `Schedule SE` (Self-Employment Tax)
    - Limitations & AMT: `Form 8582` (Passive Activity Losses), `Form 6251` (AMT), `Form 8995/8995-A` (QBI §199A)
  - [ ] **ProConnect View Toggle**: `[Show All Forms (12)]` vs `[Show Active/Edited Forms Only (N)]`

- [ ] **Task 2.2: True Statutory Cross-Form Interlinking Engine**
  - [ ] Schedule C Line 31 (Net Profit) &rarr; Flows automatically into Schedule 1 Line 3 & Schedule SE
  - [ ] Schedule E Part I Line 26 (Total Rental Real Estate) &rarr; Flows into Form 8582 (PAL limits) &rarr; Schedule 1 Line 5
  - [ ] Schedule 1 Line 10 (Total Additional Income) &rarr; Flows into Form 1040 Line 8
  - [ ] Schedule 1 Line 26 (Total Adjustments to Income) &rarr; Flows into Form 1040 Line 10 (AGI Calculation)
  - [ ] Schedule D Line 16 &rarr; Flows into Form 1040 Line 7
  - [ ] Schedule A Line 17 vs Standard Deduction ($15,000 Single / $30,000 MFJ for 2025) &rarr; Greater flows to Form 1040 Line 12
  - [ ] Form 8995/8995-A Line 39/40 &rarr; Flows into Form 1040 Line 13 (§199A Deduction)
  - [ ] Form 6251 Line 11 (Alternative Minimum Tax) &rarr; Flows into Form 1040 Schedule 2 Line 1

- [ ] **Task 2.3: Source Document Ingestion & Auto-Population Engine**
  - [ ] Create standardized JSON/PDF mock test documents:
    - `W-2` (Wages, Fed Tax, State Tax, Social Security/Medicare)
    - `1099-INT` / `1099-DIV` (Ordinary/Qualified Dividends)
    - `1099-NEC` / `1099-K` (Self-Employment Consulting)
    - `1099-B` (Stock / Crypto Sales with Box A/B/D/E)
    - `Schedule K-1 (Form 1065 / 1120-S)` (Box 1 Ordinary Income, Box 2 Rental, Box 19/20 Distributions)
    - `Form 1098` (Mortgage Interest & Real Estate Taxes)
  - [ ] Document Uploader / Sample Picker in Document Binder:
    - User can click `[Ingest Sample W-2]` or upload JSON source slip
    - Engine automatically keys values into target lines with visual pulse
    - Auto-generates line-by-line audit trail linking form inputs back to source slip

---

## 🎨 Phase 3: Ultra-Premium UI/UX (RTX 3080 3D Depth & Fluid Motion)

- [ ] **Task 3.1: Tactile 3D Buttons & Dynamic Depth Shading**
  - [ ] Primary buttons (`[+ Create Tax Return]`, `[Open Return ↗]`, `[Audit & Verify]`) get realistic tactile 3D bevels, subtle top specular highlights (`inset 0 1px 0 rgba(255,255,255,0.2)`), and pressed-state depression (`active:translate-y-0.5 active:shadow-inner`)
  - [ ] Secondary & pill buttons get subtle glass elevation with responsive hover lifts
  - [ ] Hover glow flares mapped to status (Emerald for active/compliant, Sky for open, Rose for delete/critical)

- [ ] **Task 3.2: Silky Fluid Animations & Transitions**
  - [ ] Tab switching between entities (`1040`, `1065`, `1120-S`, `Trash`) uses smooth cubic-bezier sliding indicators (`transition-all duration-300 cubic-bezier(0.16, 1, 0.3, 1)`)
  - [ ] Form-to-form transition smoothly slides canvas with zero layout jumping
  - [ ] Modals enter with smooth spring scale/fade (`scale-95 opacity-0` &rarr; `scale-100 opacity-100`)

---

## 🎙️ Phase 4: Big 4 Real-Life Mock Interview Simulator (Interactive Voice Arena)

- [ ] **Task 4.1: Voice-Driven Interactive Interview Room**
  - [ ] Top nav button: `[🎙️ Big 4 Mock Interview]` launches the Interview Arena
  - [ ] **Spoken Question Delivery (Browser TTS)**:
    - Virtual Big 4 Senior Manager / Partner asks technical tax questions out loud with speech synthesis
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
    3. *Executive Communication & Big 4 Demeanor*
  - [ ] AI delivers immediate constructive feedback, score (1–10), and asks an adaptive follow-up question
  - [ ] Includes direct sync link to your NotebookLM: `https://notebook.google.com/notebook/7f8a6c49-fbdb-4404-bd17-5512c528da00?authuser=1`

- [ ] **Task 4.3: Interactive Web Context & Line-Level Attachment Engine for Qwen 14B**
  - [ ] **Click-to-Attach**: Clicking an "Ask AI" pill on any line card attaches that line's full statutory payload (line number, description, statutory code citation, input vs computed value, cross-foot source) as an active context chip in the chat box
  - [ ] **Hover Tooltip & Hotkey (`Alt + R`)**: Hovering any field shows an interactive mini tooltip with IRC rule, and pressing `Alt + R` automatically sends that line context to Qwen 14B
  - [ ] **Drag-and-Drop Form Line onto Chat**: Dragging any line card or document slip and dropping it into the chat pane attaches it as a contextual reference
  - [ ] **Live Full-Return Snapshot**: Chat payload automatically injects active return state (AGI, Taxable Income, active diagnostic flags) so Qwen has complete visibility of the entire return without hallucinating

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
  - [ ] Hook & Story Script: "How I Built a Big-4 Grade Virtual Tax Software for ₹0 After Getting Laid Off"
  - [ ] Screen Recording storyboard & showcase clips (Obsidian Aurora theme, RTX 3080 telemetry, 1040/1065/1120-S flows, NotebookLM integration)
  - [ ] Architecture diagram & technical callouts (Antigravity + NotebookLM Ground-Truth + Argon 4 + Local Qwen 14B)

- [ ] **Task 6.2: Deep-Focus & Daily Health Productivity Companion (Web/PWA & Mobile Push)**
  - [ ] Pomodoro / Study Focus Timer tuned for deep tax return preparation
  - [ ] Mobile push reminders for study sessions via Web Push API / Telegram / Discord Webhook
  - [ ] Hydration & Ergonomic Break Reminders ("Drink water", "20-20-20 eye relief", "Stretch breaks")
  - [ ] End-of-day auto-sync to `DAILY_LEARNING_LOG.md` and GitHub
