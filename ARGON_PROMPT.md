TARGET ACTION: EDIT EXISTING FILE
TARGET FILE: d:\Tax Compliance Preparation\Apex Tax Practice Hub\index.html
SESSION NOTE: Open a FRESH session in Argon for this file.

Task 1.2: Fix Return Routing & Multi-Client Support in index.html

Currently, index.html ignores the ?return= URL parameter and hardcodes Dr. Marcus Vance on boot.
Update index.html to read the active return parameter and dynamically adjust the taxpayer identity, header, and source slips:

1. Dynamic URL & LocalStorage Parsing on Boot:
In window.onload (or app initialization):
- Read the return parameter:
  const urlParams = new URLSearchParams(window.location.search);
  const activeReturnId = urlParams.get('return') || localStorage.getItem('activeReturnId') || '1040_alex_morgan';
- Also check localStorage.getItem('activeReturnData') for any custom user-created returns.

2. Dynamic Header & Breadcrumb:
- Add a clear back-link in the top navbar:
  <a href="returns.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-mono text-emerald-400 border border-white/[0.08] transition flex items-center gap-1.5">
    <span>[← Practice Hub]</span>
  </a>
- Dynamically update the client name banner in the header based on activeReturnId:
  - If activeReturnId === '1040_alex_morgan':
    Display: "Alex Morgan" • Single • W-2 Tech Lead • TY 2025
  - If activeReturnId === '1040_marcus_vance':
    Display: "Dr. Marcus & Elena Vance" • MFJ • Healthcare & Real Estate • TY 2025
  - If activeReturnId === '1065_apex_horizon':
    Display: "Apex Horizon Partners LLC" • Form 1065 • 3 Partners • TY 2025
  - If activeReturnId === '1120s_vanguard':
    Display: "Vanguard Logic Systems Inc" • Form 1120-S • S-Corp • TY 2025
  - For custom returns: display the custom taxpayerName from activeReturnData.

3. Client-Specific Document Binder:
- When activeReturnId === '1040_alex_morgan':
  Update the Client Document Binder to show Alex Morgan's source slips:
  - W-2: BigTech Inc ($380,000 Box 1 Wages, $42,000 Fed Withholding)
  - Form 3921: ISO Stock Option Exercise (10,000 shares, $12 spread = $120,000 AMT Preference Form 6251)
  - 1099-B: Crypto & Equity Capital Gains ($45,000 net gain Schedule D)
  - 1099-NEC: Consulting Income ($65,000 Schedule C)
- When activeReturnId === '1040_marcus_vance':
  Retain Dr. Marcus & Elena Vance's existing medical practice & passive real estate syndication slips.

Preserve all existing statutory calculations, cross-footing, Qwen 14B reviewer integration, and shortcut functions.
