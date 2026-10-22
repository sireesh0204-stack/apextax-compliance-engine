# ⚡ Argon Prompt Workbench — Tax Compliance Suite

> **Status**: Form 1040 Workstation Phase 2 Enhancements Successfully Merged.  
> **Active Environment**: TY 2025 IRS Statutory Compliance Suite &bull; Obsidian Aurora Theme &bull; Local Qwen 14B Reviewer.

---

## 🛠️ Ready Template: Form 1040 Bug Fixes & Refinements (Upon Return)

*When you return from your 2-day trip, paste any specific bugs you noticed below and pass this prompt to Argon:*

```markdown
TARGET ACTION: EDIT EXISTING FILE
TARGET FILE: d:\Tax Compliance Preparation\Apex Tax Practice Hub\return_1040.html
SESSION NOTE: Open a FRESH session in Argon for this file.

CRITICAL INSTRUCTION: Provide clean, targeted replacement snippets or complete functions so they can be merged directly into `return_1040.html` without breaking any existing styling, form workpapers, or reactive recalculation logic.

Fix the following bugs identified in Form 1040 Workstation:

1. [Bug 1 Description - e.g. Specific Line Calculation / Cross-Foot Discrepancy]
2. [Bug 2 Description - e.g. UI Layout / Modal Alignment / Dual-Monitor Sync]
3. [Bug 3 Description - e.g. Telemetry Ribbon or Diagnostic Audit Tray Check]

Please output the clean targeted replacement portions for `return_1040.html`.
```

---

## 🏛️ Next Planned Module: Form 1065 Partnership & Real Estate Workstation (`return_1065.html`)

```markdown
TARGET ACTION: CREATE NEW FILE
TARGET FILE: d:\Tax Compliance Preparation\Apex Tax Practice Hub\return_1065.html
SESSION NOTE: Open a FRESH session in Argon.

Build `return_1065.html` matching the Obsidian Aurora styling of `return_1040.html` with:
1. Top Navbar with entity routing back to `returns.html`, filing status pill, and `[📂 Popout Source Documents ↗]`.
2. Left Sidebar Navigation Tree:
   - Form 1065 Page 1 (Ordinary Trade/Business Income & Deductions)
   - Form 8825 (Rental Real Estate Income and Expenses of a Partnership)
   - Schedule K (Partners' Distributive Share Items)
   - Schedule K-1 Partner Allocation Engine (Items J, K debt allocations, L capital account §704(b), M)
   - Schedule M-1 (Reconciliation of Income/Loss per Books with Income/Loss per Return)
   - Schedule M-2 (Analysis of Partners' Capital Accounts)
3. Statutory Calculations:
   - Form 8825 Line 21 net rental real estate flows directly to Schedule K Line 2
   - Section 179 deduction limitations under §179(b)(1) & (b)(2) flowing to Schedule K Line 12
   - Qualified Nonrecourse Financing (QNF) under §465(b)(6) giving at-risk basis
4. Senior Tax Compliance Reviewer AI Pane (Local Qwen 2.5 14B).
```
