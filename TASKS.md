# ⚡ ApexTax OS — Master Task Checklist & Implementation Roadmap

> **System Overview**: High-Performance, GPU-Accelerated Tax Compliance Workstation & Big 4 Defense Simulator.
> **Engine Stack**: Multi-Entity Statutory Tax Engine (TY 2025) &bull; Local Qwen 2.5 14B (`localhost:11434`) &bull; RTX 3080 Obsidian Aurora Theme.
> 
> *Instructions*: Mark an item as complete with `[x]` once verified. We will only move to the next task after you give your approval!

---

## 📌 Phase 1: Practice Hub (`returns.html`) Core Fixes

- [ ] **Task 1.1: Verify & Lock Tax Year 2025 Across Entire Practice Hub**
  - [ ] **1.1.1**: Header reads: `⚡ ApexTax Practice Hub | 2025 Tax Compliance`
  - [ ] **1.1.2**: Top KPI ribbon displays: `TY 2025 Filing Season`
  - [ ] **1.1.3**: All table row badges show `TY 2025`
  - [ ] **1.1.4**: Default year in `[+ Create Tax Return]` wizard defaults to `2025`
  - [ ] **1.1.5**: Storage key updated to purge any stale 2024 cached items from browser memory

- [ ] **Task 1.2: Fix Alex Morgan vs. Dr. Marcus Vance Redirection Bug**
  - [ ] Clicking `[Open Return ↗]` on **Alex Morgan** routes to `index.html?return=1040_alex_morgan`
  - [ ] Clicking `[Open Return ↗]` on **Dr. Marcus Vance** routes to `index.html?return=1040_marcus_vance`
  - [ ] Clicking `[Open Return ↗]` on **Apex Horizon Partners** routes to `index.html?return=1065_apex_horizon`
  - [ ] Clicking `[Open Return ↗]` on **Vanguard Logic Systems** routes to `index.html?return=1120s_vanguard`
  - [ ] `index.html` inspects URL parameters on boot and loads the correct taxpayer identity and document slips

- [ ] **Task 1.3: Delete Return / Archive & Trash Management**
  - [ ] Each table row has an action dropdown `[...]` with:
    - `📁 Archive Return`
    - `🗑️ Move to Trash`
  - [ ] Dedicated tab pill: `Archived / Trash (Count)` in entity filter bar
  - [ ] In Trash view, rows display `[Restore ↩]` and `[Permanently Delete ✖]`
  - [ ] Toast notification with `[Undo ↩]` on delete/archive
  - [ ] `[↺ Reset Master Cases]` button to safely restore default curriculum cases

---

## 🎨 Phase 2: Ultra-Premium UI/UX (RTX 3080 3D Depth & Fluid Motion)

- [ ] **Task 2.1: Tactile 3D Buttons & Dynamic Depth Shading**
  - [ ] Primary buttons (`[+ Create Tax Return]`, `[Open Return ↗]`, `[Audit & Verify]`) get realistic tactile 3D bevels, subtle top specular highlights (`inset 0 1px 0 rgba(255,255,255,0.2)`), and pressed-state depression (`active:translate-y-0.5 active:shadow-inner`)
  - [ ] Secondary & pill buttons get subtle glass elevation with responsive hover lifts
  - [ ] Hover glow flares mapped to status (Emerald for active/compliant, Sky for open, Rose for delete/critical)

- [ ] **Task 2.2: Silky Fluid Animations & Transitions**
  - [ ] Tab switching between entities (`1040`, `1065`, `1120-S`, `Trash`) uses smooth cubic-bezier sliding indicators (`transition-all duration-300 cubic-bezier(0.16, 1, 0.3, 1)`)
  - [ ] Table rows animate smoothly on search/filter with subtle staggered fade-and-slide
  - [ ] Modals (Create Return, Confirm Delete) enter with smooth spring scale/fade (`scale-95 opacity-0` ➔ `scale-100 opacity-100`)

---

## 🎙️ Phase 3: Big 4 Real-Life Mock Interview Simulator (Interactive Voice Arena)

- [ ] **Task 3.1: Voice-Driven Interactive Interview Room**
  - [ ] Top nav button: `[🎙️ Big 4 Mock Interview]` launches the Interview Arena
  - [ ] **Spoken Question Delivery (Browser TTS)**:
    - Virtual Big 4 Senior Manager / Partner asks technical tax questions out loud with speech synthesis
    - Visual speaking wave visualizer indicates AI is currently speaking
  - [ ] **Speech-to-Text Input (Browser STT / Web Speech API)**:
    - User presses mic (or holds spacebar/hotkey) and speaks their technical answer
    - Live transcription displays in real-time with waveform indicator
  - [ ] **Text Fallback**:
    - Optional keyboard input box for typing answers if working silently

- [ ] **Task 3.2: Local Qwen 14B Statutory Defense Scoring & Follow-Ups**
  - [ ] Qwen 14B analyzes spoken response across 3 dimensions:
    1. *Statutory Accuracy & IRC Code Citations* (§469, §199A, §704(b), §1368, etc.)
    2. *Audit Defense & Risk Identification*
    3. *Executive Communication & Big 4 Demeanor*
  - [ ] AI delivers immediate constructive feedback, score (1–10), and asks an adaptive follow-up question
  - [ ] Includes direct sync link to your NotebookLM: `https://notebook.google.com/notebook/7f8a6c49-fbdb-4404-bd17-5512c528da00?authuser=1`

---

## ⚡ Phase 4: Theme Harmonization Across Entire Suite

- [ ] **Task 4.1: Harmonize Return Workstation (`index.html`)**
  - [ ] Migrate `index.html` from light parchment to the **Obsidian Aurora** dark theme
  - [ ] GPU-accelerated frosted glass panels, glowing status badges, and tabular numerals
  - [ ] Clean minimalist header (no chunky bold font, no clutter)
  - [ ] Strict `100vh` viewport containment to fix split-screen scroll bugs
  - [ ] Field-level drill-down & trace-back navigation (`jumpToField` + `Alt + ←` breadcrumb)
  - [ ] Logitech MX Master 3S hotkey HUD modal (`Ctrl + Shift + H` / `?`)

- [ ] **Task 4.2: Harmonize 30-Day Master Curriculum (`curriculum.html`)**
  - [ ] Update header, cards, and day modules to match the Obsidian Aurora palette
  - [ ] Preserve all 30 days of statutory lessons, cross-foot checks, and progress checklist
  - [ ] Add quick-launch links into corresponding practice cases in `returns.html` and `index.html`

