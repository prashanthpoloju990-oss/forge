# FORGE — Changelog (Latest Release vs Previous Push)

**Commit Range**: `e0cf495` ➔ `7140eff`  
**Deployment**: Production ([forge-work.vercel.app](https://forge-work.vercel.app))  
**Total Changes**: 46 files changed (`+4,684` additions, `-1,629` deletions)

---

## 1. Executive Summary of Changes

| Area | Nature of Change | Key Files Modified / Created |
| :--- | :--- | :--- |
| **Backend Architecture** | 🚀 **NEW**: Full FastAPI (Python 3.11) Backend with Multi-Agent OS & Monte Carlo Simulation | `backend/main.py`, `backend/storage.py`, `backend/services/*`, `backend/routers/*` |
| **Frontend API Layer** | 🔌 **NEW**: Type-safe REST client & Vite proxy | `src/api/forgeApi.ts`, `vite.config.ts`, `package.json` |
| **Investor Memo Studio** | 📑 **NEW**: Autonomous Board Memo & PDF Dispatch Engine | `src/components/dashboard/InvestorMemoModal.tsx` |
| **Landing Page Overhaul** | 🎨 **REFACTORED**: Fluid Open Editorial Layout (Zero Box/Card Fatigue) | `Problem.tsx`, `Introducing.tsx`, `HowItWorks.tsx`, `OperatingSuite.tsx`, `Footer.tsx`, `FinalCTA.tsx` |
| **Dashboard Views** | ⚡ **UPGRADED**: Segmented Sub-Navigation Architecture & Borderless Ribbons | `OverviewView.tsx`, `FinanceView.tsx`, `HiringView.tsx`, `LegalView.tsx`, `MarketingView.tsx`, `TopSnapshot.tsx` |
| **Creation Studios** | ✨ **UPGRADED**: Interactive multi-step creation studios with real-time impact calculations | `CreateDocumentModal.tsx`, `CreateRoleModal.tsx`, `CreateCampaignModal.tsx`, `AddSnapshotModal.tsx`, `CreateEventModal.tsx` |
| **Visual Craft & FX** | 💎 **ENHANCED**: Multi-layer Liquid Glass styling with specular highlights & login illustration | `src/index.css`, `public/illustrations/login-portal.png`, `LoginPage.tsx`, `Navbar.tsx`, `TopBar.tsx` |

---

## 2. Detailed File-by-File Breakdown

### A. Python Backend (`backend/`) [NEW MODULE]
* `backend/main.py`: FastAPI server setup with CORS, health diagnostics (`GET /api/health`), OpenAPI docs (`/docs`), and root redirect.
* `backend/storage.py`: In-memory & JSON persistent company graph storage.
* `backend/requirements.txt`: Python package dependencies (`fastapi`, `uvicorn`, `pydantic`, `numpy`, `httpx`).
* `backend/services/agent_orchestrator.py`: Multi-Agent intent parser coordinating domain agents (*Legal Shield*, *Treasury Solver*, *Talent Architect*).
* `backend/services/monte_carlo_engine.py`: 1,000-run Monte Carlo cash simulator with confidence bands (`p10`, `p50`, `p90`).
* `backend/services/delaware_legal_engine.py`: Delaware contract synthesizer for SAFE notes, NDAs, and contractor IP assignments.
* `backend/routers/command.py`: `POST /api/command` and `POST /api/command/execute` endpoints.
* `backend/routers/finance.py`: `GET /api/finance/snapshot` and `POST /api/finance/simulate` endpoints.
* `backend/routers/legal.py`: `GET /api/legal/documents` and `POST /api/legal/generate` endpoints.
* `backend/routers/hiring.py`: `GET /api/hiring/roles` and `POST /api/hiring/roles` endpoints.
* `backend/routers/investor.py`: `GET /api/investor/memo` autonomous update generator.

---

### B. Landing Page Components (`src/components/`)
* `src/components/Problem.tsx`:
  * Removed all 4 clunky card boxes.
  * Converted into an open, spacious 2-column editorial narrative (`§01 Spreadsheet Runway Drift`, `§02 Hiring Loop Fragmentation`, `§03 Ad-hoc Legal Friction`, `§04 Operational Context Switching`).
* `src/components/Introducing.tsx`:
  * Removed enclosing box frames and rigid absolute positioning.
  * Refactored into a rock-solid, responsive 3-column layout with open metrics (`$284,500`), live sparklines, and uncompressed copy.
* `src/components/HowItWorks.tsx`:
  * Transformed simple icon circles into an open **4-Stage Architectural Pipeline** (`§01 Input Layer`, `§02 Intelligence Layer`, `§03 Synthesis Layer`, `§04 Execution Layer`) with interactive wireframe previews.
* `src/components/OperatingSuite.tsx` [NEW]:
  * Consolidated the 3 full-height repetitive department sections into a single interactive 3-in-1 Operating Suite, eliminating scroll fatigue by 65%.
* `src/components/Footer.tsx`:
  * Redesigned into a multi-column editorial footer with platform navigation, live system health pill, and direct `⌘K` founder console card.
* `src/components/FinalCTA.tsx`:
  * Redesigned into an inspiring hero banner with trust badges (*Zero spreadsheet friction*, *Delaware C-Corp compliant*, *Instant 1-click approvals*) and dual CTA buttons.
* `src/components/LoginPage.tsx`:
  * Replaced duplicated hero graphic with bespoke `/illustrations/login-portal.png`.
* `src/components/Navbar.tsx`:
  * Upgraded floating header with `.glass-liquid` multi-pass frosted blur.

---

### C. Dashboard Components (`src/components/dashboard/`)
* `src/components/dashboard/TopSnapshot.tsx`:
  * Refactored metric tiles from separate cards into an open, borderless metric ribbon separated by clean vertical rules.
* `src/components/dashboard/NeedsAttention.tsx` & `OperatingPulse.tsx`:
  * Removed heavy box card enclosures in favor of open divider feed layouts.
* `src/components/dashboard/OverviewView.tsx`:
  * Integrated the `[ ✨ Generate Investor Memo ]` action button and refactored right-side illustration block.
* `src/components/dashboard/InvestorMemoModal.tsx` [NEW]:
  * Multi-format board memo generator (Executive Document View, Raw Markdown, Email Template) with one-click clipboard copy and print/PDF export.
* `src/components/dashboard/ForgeCommand.tsx`:
  * Upgraded to floating `.glass-liquid` capsule with prompt suggestion chips.
* `src/components/dashboard/Sidebar.tsx` & `ProductPreview.tsx`:
  * Removed redundant `ACME.INC` box under the FORGE logo.
* `src/components/dashboard/finance/FinanceView.tsx`:
  * Added segmented sub-navigation (`Runway & Forecast`, `Cash Ledger & Activity`, `Treasury Guardian`) and `[ 📄 Export Memo ]` trigger.
* `src/components/dashboard/hiring/HiringView.tsx`:
  * Added segmented sub-navigation (`Candidate Pipeline`, `Open Headcount & Roles`, `Sourcing Intelligence`).
* `src/components/dashboard/legal/LegalView.tsx`:
  * Added segmented sub-navigation (`Active Contracts & Preview`, `Execution & Workflow`, `Delaware Compliance`).
* `src/components/dashboard/marketing/MarketingView.tsx`:
  * Added segmented sub-navigation (`Campaigns & Preview`, `Content Workspace & Drafts`, `Narrative Intelligence`).

---

### D. Interactive Creation Studios (`src/components/dashboard/*/`)
* `CreateDocumentModal.tsx`: Upgraded into a Delaware Document Studio with templates, AI assist, and interactive protective clause toggles.
* `CreateRoleModal.tsx`: Upgraded into a Talent Studio with real-time runway impact calculations and skill chips.
* `CreateCampaignModal.tsx`: Upgraded into a Growth Campaign Studio with archetypes and multi-channel deliverables.
* `AddSnapshotModal.tsx`: Upgraded into a Treasury Calibration Studio with live runway recalculation.
* `CreateEventModal.tsx`: Upgraded into an Executive Schedule Studio with presets and Google Meet integration.

---

### E. Configuration & Styling
* `src/index.css`: Added multi-layer liquid glass utilities (`.glass-liquid`, `.glass-pill`, `.glass-modal`) and print stylesheets (`@media print`).
* `src/api/forgeApi.ts` [NEW]: Type-safe frontend client for backend communication.
* `src/services/commandService.ts`: Connected `executeCommand` directly to FastAPI backend with fallback resilience.
* `vite.config.ts`: Configured `/api` reverse proxy to `http://127.0.0.1:8000`.
* `package.json`: Added `npm run server` and `npm run server:prod` scripts.
* `.gitignore`: Added Python ignores (`__pycache__`, `*.pyc`, `backend/data/`).
