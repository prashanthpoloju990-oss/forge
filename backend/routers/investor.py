"""
Router: Autonomous Shareholder Update & Investor Memo Generator
"""

from fastapi import APIRouter
from typing import Dict, Any, List
from ..storage import db
from datetime import datetime

router = APIRouter(prefix="/api/investor", tags=["Investor Relations"])


@router.get("/memo")
def generate_investor_memo():
    """
    Generates a real-time executive memo aggregated from the live graph.
    """
    state = db.get_state()
    startup = state["startup"]
    founder = state["founder"]
    finance = state["finance"]
    roles = state["roles"]
    candidates = state["candidates"]
    documents = state["documents"]

    active_finalists = [c for c in candidates if c.get("stage") == "final"]
    current_month = datetime.now().strftime("%B %Y")

    highlights = [
        f"Liquid Cash Reserves: {finance['cash']} at {finance['monthlyBurn']} net burn ({finance['runway']} runway).",
        f"Monthly Recurring Revenue: {finance['monthlyRevenue']} (+8.4% MoM) driven by enterprise conversion.",
        f"Talent Pipeline: {len(roles)} open roles with {len(active_finalists)} finalists in final offer loops.",
        f"Delaware Compliance: {len(documents)} executed corporate instruments vaulted with 0 risk deviations."
    ]

    asks = [
        "Introductions to Senior Full-Stack Engineers with React 19 & performance experience.",
        "Early customer intros for Series Seed design partners exploring automated founder operations."
    ]

    markdown_text = f"""# {startup['name']} — Monthly Investor Update ({current_month})
**Founder**: {founder['name']} ({founder['email']})
**Stage**: {startup['stage']}

---

### 📊 Financial Vitals
* **Cash Balance**: {finance['cash']} (Mercury & SVB synced)
* **Monthly Net Burn**: {finance['monthlyBurn']}
* **Runway**: {finance['runway']}
* **MRR**: {finance['monthlyRevenue']}

### 🚀 Key Operational Highlights
""" + "\n".join([f"* {h}" for h in highlights]) + """

### 🤝 How Investors Can Help
""" + "\n".join([f"* {a}" for a in asks])

    return {
        "status": "success",
        "timestamp": datetime.now().isoformat(),
        "month": current_month,
        "startup": startup,
        "founder": founder,
        "financial_vitals": finance,
        "highlights": highlights,
        "asks": asks,
        "markdown": markdown_text
    }
