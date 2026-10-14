# ⚡ ApexTax Spatial Workstation — Big 4 Tax Compliance Tracker

- **Last Synchronized**: `2026-10-15T02:05:00.000Z`
- **Completion Progress**: **0 / 12 Days (0%)**

## Phase 1: Individual

- [ ] **Day 01: Form 1040 Total Income, AGI & Tax Computation** | `IRC §1, §61, §62, §63` | Line 1z, 9, 10, 11b, 12, 13a, 15, 16
- [ ] **Day 02: Self-Employment Tax & Schedule SE Computation** | `IRC §1401, §1402(a), §164(f)` | Lines 3, 4a (92.35%), 4c, 12; Sched 1 Line 15 (50%)
- [ ] **Day 03: Section 199A QBID Basics & Form 8995** | `IRC §199A, §62(a)(20)` | 20% of QBI vs 20% of (Taxable Income - Net Cap Gains)

## Phase 2: Depreciation/Investments

- [ ] **Day 04: Form 4562 Section 179 & MACRS Depreciation** | `IRC §179, §168(k), §280F` | $2.5M cap, $4.0M phaseout threshold, taxable income limit
- [ ] **Day 05: Schedule C, Schedule D / Form 8949 & Capital Gains Tax** | `IRC §1211(b), §1221, §1231` | $3,000 net capital loss limit ($1,500 MFS), Form 4797
- [ ] **Day 06: Alternative Minimum Tax (AMT) & Form 6251** | `IRC §55, §56, §57, §58` | AMTI calculation, SALT addback, 26%/28% dual rate

## Phase 3: Pass-Through & Loss Ordering

- [ ] **Day 07: Form 1065 Partnership Tax, Schedule K/K-1 & Pub 541** | `IRC §701, §702, §704(b), §707(c), §743(b), §754` | Guaranteed payments, General vs Limited partner SE tax
- [ ] **Day 08: Form 1120-S S-Corporation Tax & Schedule K/K-1** | `IRC §1361, §1362, §1366, §1367, §1368` | Officer compensation vs distributions audit trap
- [ ] **Day 09: Tier 1 Loss Limitation — Form 7203 S-Corp Basis** | `IRC §1366(d), §1367` | Ordering: Basis -> Distributions -> Nondeductibles -> Loss
- [ ] **Day 10: Tier 2 Loss Limitation — Form 6198 At-Risk Limitations** | `IRC §465, §465(b)(6)` | Qualified nonrecourse financing, nonrecourse debt exclusions
- [ ] **Day 11: Tier 3 Loss Limitation — Form 8582 Passive Activity Losses** | `IRC §469, §469(i), §469(g)` | $25k rental allowance with $100k-$150k MAGI phaseout

## Phase 4: Corporate & M-1

- [ ] **Day 12: Schedule M-1 / M-3 Reconciliation & Tier 4 Excess Business Loss** | `IRC §461(l), §163(j), §263A, §274` | 4-Tier Master Cascade, $305k ($610k MFJ) EBL limit

---

## The 4-Tier Master Loss Cascade Architecture
$$\text{Raw K-1 Loss} \xrightarrow{\text{Tier 1: §1366(d)/§704(d) Basis (Form 7203)}} \xrightarrow{\text{Tier 2: §465 At-Risk (Form 6198)}} \xrightarrow{\text{Tier 3: §469 Passive (Form 8582)}} \xrightarrow{\text{Tier 4: §461(l) EBL (Form 461)}} \text{Taxable Income Reduction}$$
