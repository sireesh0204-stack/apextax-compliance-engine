# ⚡ ApexTax Spatial Workstation — Big 4 Tax Compliance Tracker (30-Day Master Roadmap)

- **Last Synchronized**: `2026-10-15T03:30:00.000Z`
- **Completion Progress**: **0 / 30 Days (0%)**
- **Core Entities**: High-Net-Worth Individuals (1040), Partnerships & Real Estate (1065), S-Corporations & Basis (1120-S/7203)

---

## Block 1: Complex Form 1040 (HNIs & Flow-Through Ingestion) [Days 01–08]

- [ ] **Day 01: Form 1040 Core Architecture & Gross Income (§61)** | `IRC §1, §61, §152` | Filing Statuses, Dependency Tests, Line 1z Wages, Baseline Return Setup
- [ ] **Day 02: W-2, 1099-INT, 1099-DIV & Schedule B** | `IRC §61(a)(4), §61(a)(7), Form 1040 Line 2b/3b` | Schedule B Part I & II, Qualified vs Ordinary Dividends, Part III Foreign Accounts & FBAR
- [ ] **Day 03: Schedule A Itemized Deductions & Phaseouts** | `IRC §163(h), §164(b)(6), §170(b)` | SALT $40k base with 30% phaseout over $500k MAGI to $10k floor; $750k acquisition mortgage limit; Charity 60%/30%
- [ ] **Day 04: Schedule C & Schedule SE Self-Employment Tax** | `IRC §162, §1401, §1402(a)` | Schedule C trade/business deductions, 92.35% SE multiplier, $176,100 Social Security cap, Line 15 50% deduction
- [ ] **Day 05: Schedule D & Form 8949 Capital Transactions** | `IRC §1091, §1202, §1211(b), §1221` | Wash Sales (Code W), QSBS (Code Q), $3k net capital loss cap, 28% collectibles, Unrecaptured §1250 gain
- [ ] **Day 06: Section 199A QBID (Form 8995 & Form 8995-A)** | `IRC §199A, §62(a)(20)` | Simplified 20% calculation vs. Complex W-2 wage/UBIA limits, SSTB phaseout ($394,600–$494,600 MFJ)
- [ ] **Day 07: Form 6251 Alternative Minimum Tax (AMT)** | `IRC §55, §56, §57, §58` | AMTI addbacks (SALT, ISO exercise spreads §56(b)(3)), $137,000 exemption 25% phaseout over $1,252,700, 26%/28% dual rates
- [ ] **Day 08: Form 8960 (NIIT 3.8%) & Form 8959 + Client Return 1** | `IRC §1411, §3101(b)(2)` | 3.8% NIIT on lesser of NII or MAGI excess over $250k; 0.9% Additional Medicare; Complete Dr. Marcus Vance 1040 Execution

---

## Block 2: Complex Form 1065 & Real Estate Entities [Days 09–18]

- [ ] **Day 09: Form 1065 Core Architecture & Trade/Business Operations** | `IRC §701, §702, §703` | Page 1 Trade/Business Deductions (Lines 9–21) vs. Schedule K Separately Stated Pass-Through Items
- [ ] **Day 10: Form 8825 Rental Real Estate Deep-Dive** | `Form 8825 Lines 1–24, Schedule K Line 2` | Property-by-property unbundling, gross rents, operating expenses, mortgage interest, and net flow to Schedule K Line 2
- [ ] **Day 11: Form 4562 Cost Segregation & Bonus Depreciation in Real Estate** | `IRC §168(k), §168(e), §179` | 27.5-yr Residential vs 39-yr Commercial, 15-yr Land Improvements, 100% Bonus Depreciation, §179 rental restrictions
- [ ] **Day 12: Guaranteed Payments (§707(c)) & General vs. Limited Partner SE Tax** | `IRC §707(c), §1402(a)(13)` | Page 1 Line 10 deduction, Schedule K Line 4a-c, General Partner (Box 1 + Box 4) vs. Limited Partner (Box 4 only) SE tax
- [ ] **Day 13: Schedule K-1 Part II Item K: Debt Allocations under §752** | `IRC §752, §465(b)(6), Treas. Reg. §1.752-2` | Recourse liabilities, Nonrecourse liabilities, and Qualified Nonrecourse Financing (QNF) that creates At-Risk Basis
- [ ] **Day 14: Schedule K-1 Part II Item L: Mandatory Tax Basis Capital Accounts** | `Notice 2020-43, Form 1065 Item L` | Tax Basis Method roll-forward equation, negative capital accounts, and Deficit Restoration Obligations (DROs)
- [ ] **Day 15: Section 704(b) Book Capital vs. Section 704(c) Built-In Gains** | `IRC §704(b), §704(c), Treas. Reg. §1.704-3` | Pre-contribution gain tracking, traditional/remedial depreciation allocations, Schedule K-1 Box 20 Code AA
- [ ] **Day 16: Section 754 Election & §743(b)/§734(b) Inside Basis Step-Ups** | `IRC §754, §743(b), §755` | Calculating transferee basis adjustment, §755 two-class asset allocation, Schedule K-1 Box 11 Code F / Box 20 Code U
- [ ] **Day 17: Section 1031 Like-Kind Exchanges for Real Estate (Form 8824)** | `IRC §1031, Form 8824 Lines 1–25` | 45-day ID / 180-day closing rules, boot received (cash + net debt relief), realized vs recognized gain, replacement basis
- [ ] **Day 18: Form 1065 Schedule M-1 / M-3 Reconciliations + Client Return 2** | `Form 1065 Schedule M-1/M-2/M-3` | Book-to-tax permanent vs temporary differences; Complete Apex Horizon Commercial Real Estate Fund LP Return Execution

---

## Block 3: Complex Form 1120-S & The 4-Tier Master Loss Cascade [Days 19–25]

- [ ] **Day 19: Form 1120-S Core Architecture & Officer Reasonable Compensation** | `IRC §1361, §1366(e), Form 1125-E` | Page 1 Line 7 / Form 1125-E vs. Schedule K-1 Box 16 Code D distributions audit trap; single class of stock rules
- [ ] **Day 20: >2% Shareholder Health Insurance & Fringe Benefits** | `IRC §1372, Notice 2008-1` | W-2 Box 1 wage addback, FICA/FUTA exemption, Page 1 Line 7 deduction, and Form 1040 Schedule 1 Line 17 deduction
- [ ] **Day 21: Tier 1 Loss Limitation — Form 7203 Part I Stock Basis Roll-Forward** | `IRC §1366(d), §1367, Form 7203 Part I` | Strict 4-step sequence: Income -> Distributions -> Nondeductibles -> Losses; excess distributions as capital gain
- [ ] **Day 22: Tier 1 Loss Limitation — Form 7203 Part II Debt Basis Mechanics** | `IRC §1367(b)(2), Treas. Reg. §1.1367-2` | Direct loans vs. Open Account Debt ($25k threshold), debt basis restoration before stock basis, guarantee zero-basis rule
- [ ] **Day 23: Tier 2 (Form 6198 At-Risk) & Tier 3 (Form 8582 Passive Activity Losses)** | `IRC §465, §469, §469(i)` | Nonrecourse debt exclusions; PAL netting; $25k active rental real estate allowance with $100k–$150k MAGI phaseout
- [ ] **Day 24: Tier 4 (Form 461 Excess Business Loss) & Schedule M-2 Equity Buckets** | `IRC §461(l), §1368` | $313,000 / $626,000 (MFJ) loss cap to NOL; Schedule M-2 4-tier equity ordering: AAA vs. PTEP vs. AE&P vs. OAA
- [ ] **Day 25: Form 1120-S / Form 7203 Comprehensive Execution + Client Return 3** | `Form 1120-S, Form 7203, Schedule E` | Complete Vanguard Precision Manufacturing Inc. Return Execution & Shareholder Form 7203/1040 flow-through

---

## Block 4: Corporate Form 1120, Multi-State, Tax Tech & Mock Interview [Days 26–30]

- [ ] **Day 26: Form 1120 C-Corporation Core Compliance** | `IRC §11, §243, Form 1120 Lines 1–31` | Flat 21% tax rate, corporate filing deadlines, Dividends Received Deduction (DRD §243), charitable 10% taxable income limit
- [ ] **Day 27: Corporate Net Operating Losses (NOL §172) & Schedule M-1/M-3** | `IRC §172, Form 1120 Schedule M-1/M-3` | 80% taxable income limitation, indefinite carryforward tracking, permanent vs. temporary corporate differences
- [ ] **Day 28: Multi-State Apportionment & State K-1 Equivalents** | `UDITPA, State Sourcing Rules` | 3-factor (Property, Payroll, Sales) vs. Single Sales Factor formulas, market-based sourcing vs. cost of performance
- [ ] **Day 29: Tax Technology Architecture: AST Rule Engines & Automated Testing** | `Tax Engine Architecture, MeF XML` | Translating statutory logic into deterministic AST rule engines, MeF XML schema validation, golden-file regression harness
- [ ] **Day 30: 60-Minute Comprehensive Mock Technical Interview with Big 4 Senior Manager** | `All Covered Forms & Code Sections` | Full Socratic partner interview simulation, technical position defense, and portfolio showcase
