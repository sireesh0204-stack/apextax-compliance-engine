# Career & Project Master Context: Sireesh Kumar Anasuri

> **Confidential Professional Portfolio & Project Ground Truth**  
> *Keep this file in the project repository as the permanent record of background, career strategy, industry translation, and preparation goals.*

---

## 1. Professional Background & Strengths

* **Candidate**: Anasuri Sireesh Kumar (Hyderabad, India | +91 86861 37374 | Sireesh0204@gmail.com)
* **Education**: Bachelor of Science in Mathematics, Physics & Computer Science (Acharya Nagarjuna University)
* **Core Career Profile**: 
  - **Senior Tax Analyst & Tax Form Implementation Engineer** at **Instead India Tax (Corvee)** (2025–2026): Authored 400+ production Go calculation files across 27 states, DC, and 7 municipal regimes. Owned IRS Form 1120-S, Form 7203 (S-Corp basis), Form 6198 (At-Risk), Form 2441, Form 8949, California 100S/540, and MeF XML e-file generation.
  - **US Tax Analyst** at **H&R Block** (via Nuvento & Speridian, 2023–2025): Executed Test Reconciliation Cases (TRC) on Blockworks; led state Department of Revenue (DOR) ATS certification testing across Forms 1040, 1041, 1065, 1120, 1120-S.
  - **Senior Tax Analyst** at **WayToTax Services** (2020–2023): Prepared Form 1040s, reviewed complex federal and multi-state partnership returns (Form 1065), and performed GAAP-to-IRC Book-to-Tax reconciliations.
  - **Data Analyst** at **Zen3 / Unify** (2018–2019): NLP speech-language training datasets for Apple Siri and Microsoft Cortana.

### The "Secret Weapon" Positioning (How to Pitch in Interviews)
Most tax preparers know *what buttons to click* in software (like GoSystem, Axcess, or UltraTax) but have zero clue how the calculation engine actually executes underneath.  
**Sireesh's unique edge:** You literally **built and certified the underlying calculation engines** in Go, tested against IRS/DOR Modernized e-File (MeF) schemas, and validated the mathematical logic line-by-line against IRS instruction books. When preparing or reviewing a return, you understand:
1. Exactly which IRS line items feed into which worksheets.
2. The exact statutory ordering of loss limitations (Basis $\rightarrow$ At-Risk $\rightarrow$ PAL $\rightarrow$ Excess Business Loss).
3. How Book-to-Tax differences (M-1/M-3) flow to Schedule K and individual 1040 Schedule E Page 2.

---

## 2. Immediate Career Objective & Financial Urgency

* **Current Situation**: In transition (jobless as of late 2026); family provider; urgent need to secure a high-impact role.
* **Target Roles**:
  1. **Tax Technology & Transformation (TTT)** — Senior Associate / Manager (Big 4: PwC, EY, Deloitte, KPMG; Top 10: BDO, RSM, Baker Tilly, Grant Thornton).
  2. **US Corporate & Pass-Through Tax Compliance** — Senior Tax Associate / Tax Manager (1065, 1120-S, 1040 HNI).
  3. **AI Tax Evaluation & Harness Engineer** — Evaluating AI agents on tax compliance logic and deterministic tax reasoning.
* **Core Entity Focus for Fast-Track Mastery**:
  - **Form 1040 (HNIs)**: High-Net-Worth Individuals with multi-tier K-1s, capital gains, AMT, and real estate.
  - **Form 1065**: Complex Partnerships, Real Estate Syndicates, §704(b)/(c) capital accounts, §754/§743(b) step-ups.
  - **Form 1120-S**: S-Corporations, Shareholder Basis (Form 7203), Officer Compensation vs. Distributions.

---

## 3. Decoding Job Descriptions: The "Real Estate" Mystery

### Why Job Postings say "Real Estate" instead of Form Names
In public accounting (Big 4 & Mid-Tier firms), tax practice groups are organized **by industry vertical**, not by IRS form number:
* **Asset & Wealth Management (AWM)**: Hedge funds, private equity $\rightarrow$ Form 1065, Schedule D, Section 1061 carried interest.
* **Real Estate (RE)**: Property holding companies, development funds, syndicates $\rightarrow$ Form 1065, Form 1120-S, Form 8825.
* **Commercial / Manufacturing**: Operating businesses, inventory $\rightarrow$ Form 1120, Form 1120-S, §263A UNICAP, multi-state apportionment.
* **Private Client Services (PCS) / High-Net-Worth (HNW)**: Business owners & families $\rightarrow$ Form 1040, Form 1041 (Trusts), Form 709 (Gifts).

### The Real Estate Tax Translation Matrix

| What the JD Says | The Exact IRS Forms Required | Key IRC Code Sections | What the Interviewer Wants to Hear |
| :--- | :--- | :--- | :--- |
| **"1065 & 1120S (Real Estate)"** | Form 1065 / 1120-S, **Form 8825**, Form 4562, Form 8582 | §168(k), §465, §469, §704, §752, §1031 | You know rental real estate does **not** go on Page 1 Line 1a; it goes on **Form 8825** and nets to **Schedule K Line 2**. |
| **"Depreciation & Cost Segregation"** | Form 4562 Part III & V | §168(e), §168(k), §179 | 27.5-yr Residential Rental vs. 39-yr Nonresidential Real Property; 15-yr Land Improvements; Bonus Depreciation eligibility (§179 is restricted on rental property). |
| **"Debt Allocations / Basis"** | Schedule K-1 Part II Item K, Form 6198, Form 7203 | §465(b)(6), §752 | Real estate qualifies for **Qualified Nonrecourse Financing (QNF)** under §465(b)(6), which gives At-Risk basis even without personal guarantees! |
| **"Passive Losses & RE Professional"** | Form 8582 Lines 1-3 & Part II | §469(i), §469(c)(7) | $25,000 active rental allowance (phased out between $100k–$150k MAGI); **Real Estate Professional Status (REPS)** requires 750 hours + >50% personal service time to convert rental losses to non-passive. |
| **"1031 Exchange"** | Form 8824 (Like-Kind Exchanges) | §1031, §1031(d) | Deferring gain on real property held for productive use in a trade/business or investment; 45-day identification and 180-day closing deadlines. |
| **"§754 Step-Up"** | Schedule K-1 Box 20 Code U | §754, §743(b), §734(b), §755 | Optional basis adjustment when a partner buys an interest or receives a distribution; step-up allocated between capital gain assets and ordinary income property. |
| **"Affordable Housing / LIHTC"** | Form 8586, Form 8609-A | §42 | Low-Income Housing Tax Credit allocated over a 10-year period with a 15-year compliance period. |

---

## 4. Software & Simulation Ecosystem

```
IRS PDFs & Codebooks ──► [NotebookLM: Tax Data Extractor]
                                    │
                                    ▼ (Raw Tax Facts & Citations)
                       [Antigravity: Lead Architect] ──► Generates Master Code & Prompts
                                    │
                                    ▼
                         [Argon 4: UI Developer]
                                    │
                                    ▼
                 [Spatial Curriculum & Tax Workstation]
                                    ▲
                                    │ (Review & Audit Bridge)
                       [Local Qwen 14B: Senior Reviewer]
```

---

## 5. Daily Commitment & Accountability Rules

1. **Every Day has a Practical Output**: Never just read tax theory; prepare an actual mock return or schedule on the workstation.
2. **Document Every Milestone**: Maintain `DAILY_LEARNING_LOG.md` recording every form mastered, lines reconciled, and traps defeated.
3. **Big 4 Interview Readiness**: End every study day by answering the Socratic interview questions aloud or in writing to build executive presence for managerial interviews.

