# Big 4 Tax Compliance & Technology Preparation: Curriculum & Tracker

## Status Overview
- **Track**: US Tax Compliance (Forms 1040, 1065, 1120-S, 4562, 6198, 7203, 8582, 461, M-1/M-3) & Tax Technology Engineering
- **Architecture**: Spatial UI Tax Workstation (`index.html`) with Embedded Local Qwen 14B Reviewer Bridge
- **Personas**:
  - **Argon 4**: System Architect & Code Generator
  - **Qwen 14B (Local)**: Senior Tax Reviewer & Compliance Auditor
  - **NotebookLM 1**: Big 4 Technical Interviewer (Partner / Senior Manager)
  - **NotebookLM 2**: Client ATS Scenario Generator (Fact Patterns & Source Documents)
  - **NotebookLM 3**: Statutory Rule Extractor (IRC Brackets, AST & Formulas)
  - **You**: Lead Tax Preparer & Software Engineer

---

## 4-Phase Authoritative Statutory Curriculum

### Phase 1: Individual Core & Schedules (Forms 1040, Schedule SE, §199A)
- [ ] **Day 01**: Form 1040 Total Income, AGI & Tax Computation (Line 1z, 9, 10, 11b, 12, 13a, 15, 16; IRC §1, §61, §62, §63)
- [ ] **Day 02**: Self-Employment Tax & Schedule SE Computation (Part I Line 3, 4a, 4c, 12; 92.35% factor, Social Security wage base cap; IRC §1401, §1402(a), §164(f))
- [ ] **Day 03**: Section 199A QBID Basics & Form 8995 (20% QBI vs. 20% Taxable Income less Net Capital Gains; IRC §199A, §62(a)(20))

---

### Phase 2: Depreciation, Small Business & Investments (Forms 4562, Schedule C/D, AMT)
- [ ] **Day 04**: Form 4562 Section 179 & MACRS Depreciation ($2.5M cap, $4.0M phaseout threshold, active business income limit; IRC §179, §168(k), §280F)
- [ ] **Day 05**: Schedule C, Schedule D / Form 8949 & Capital Gains Tax ($3k capital loss limit, Form 4797 §1231 netting sequence; IRC §1211(b), §1221, §1222, §1231)
- [ ] **Day 06**: Alternative Minimum Tax (AMT) & Form 6251 (AMTI, SALT addback, 26%/28% dual-rate brackets, Form 8801 MTC; IRC §55, §56, §57, §58)

---

### Phase 3: Pass-Through Entities & Loss Orderings (Forms 1065, 1120-S, 6198, 7203, 8582)
- [ ] **Day 07**: Form 1065 Partnership Tax, Schedule K/K-1 & Pub 541 (Guaranteed Payments, General vs. Limited partner SE tax; IRC §701, §702, §704(b), §707(c), §743(b), §754)
- [ ] **Day 08**: Form 1120-S S-Corporation Tax & Schedule K/K-1 (Officer compensation vs. distributions audit trap; IRC §1361, §1362, §1366, §1367, §1368)
- [ ] **Day 09**: Tier 1 Loss Limitation — Form 7203 S-Corp Stock & Debt Basis (Ordering: Basis -> Distributions -> Nondeductible -> Losses; IRC §1366(d), §1367)
- [ ] **Day 10**: Tier 2 Loss Limitation — Form 6198 At-Risk Limitations (Qualified nonrecourse financing, nonrecourse debt exclusions, §465(e) recapture; IRC §465)
- [ ] **Day 11**: Tier 3 Loss Limitation — Form 8582 Passive Activity Losses ($25,000 active rental allowance, $100k-$150k MAGI phaseout, complete disposition §469(g); IRC §469)

---

### Phase 4: Corporate Compliance, M-1/M-3 Differences & Big 4 Readiness
- [ ] **Day 12**: Schedule M-1 / M-3 Reconciliation & Tier 4 Excess Business Loss (§461(l) $305k/$610k cap, 4-tier master cascade, book-tax perm vs. temp; IRC §461(l), §163(j), §263A, §274)

---

## The 4-Tier Master Loss Cascade Architecture
$$\text{Raw K-1 Loss} \xrightarrow{\text{Tier 1: §1366(d)/§704(d) Basis (Form 7203)}} \xrightarrow{\text{Tier 2: §465 At-Risk (Form 6198)}} \xrightarrow{\text{Tier 3: §469 Passive (Form 8582)}} \xrightarrow{\text{Tier 4: §461(l) EBL (Form 461)}} \text{Taxable Income Reduction}$$
