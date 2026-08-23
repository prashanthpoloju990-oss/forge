"""
FORGE In-Memory & JSON Persistent Storage Layer
Maintains the live operational graph: Treasury, Talent, Legal, Approvals & Activity Logs.
"""

import json
import os
from typing import Dict, Any, List

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
STORAGE_FILE = os.path.join(DATA_DIR, "company_graph.json")

DEFAULT_STATE: Dict[str, Any] = {
    "startup": {
        "name": "Acme Inc.",
        "stage": "Seed Stage · Delaware C-Corp",
        "established": "2025",
        "ein": "XX-XXXXXXX"
    },
    "founder": {
        "name": "Sarah Lin",
        "email": "sarah@acme.inc",
        "role": "Founder & CEO"
    },
    "finance": {
        "cash": "$284,500",
        "monthlyBurn": "$19,200",
        "runway": "14.8 months",
        "monthlyRevenue": "$8,400",
        "lastUpdated": "Today, 10:42 AM"
    },
    "roles": [
        {
            "id": "role-1",
            "title": "Staff Frontend Engineer",
            "department": "Engineering",
            "location": "San Francisco, CA (Hybrid)",
            "type": "Full-time",
            "salary": "$175,000",
            "equity": "0.85%",
            "activeCandidates": 4,
            "status": "Open",
            "hiringLead": "Sarah Lin"
        },
        {
            "id": "role-2",
            "title": "Lead Product Designer",
            "department": "Design",
            "location": "Remote (US)",
            "type": "Full-time",
            "salary": "$160,000",
            "equity": "0.65%",
            "activeCandidates": 6,
            "status": "Open",
            "hiringLead": "Sarah Lin"
        },
        {
            "id": "role-3",
            "title": "Systems / Backend Architect",
            "department": "Engineering",
            "location": "San Francisco, CA",
            "type": "Full-time",
            "salary": "$185,000",
            "equity": "0.90%",
            "activeCandidates": 3,
            "status": "Open",
            "hiringLead": "Sarah Lin"
        }
    ],
    "candidates": [
        {
            "id": "cand-1",
            "name": "Aisha Khan",
            "roleId": "role-1",
            "stage": "final",
            "consensus": "Strong Yes (4/4)",
            "score": "4.9/5.0",
            "notes": "Exceptional systems architecture and typography craft. Ex-Stripe.",
            "nextStep": "Offer decision approval"
        },
        {
            "id": "cand-2",
            "name": "Marcus Vance",
            "roleId": "role-2",
            "stage": "final",
            "consensus": "Yes (3/4)",
            "score": "4.6/5.0",
            "notes": "Strong editorial design portfolio and Figma system design skills.",
            "nextStep": "Founder final conversation"
        }
    ],
    "documents": [
        {
            "id": "doc-1",
            "title": "Series Seed Mutual NDA · Foundry Group",
            "type": "Mutual Non-Disclosure Agreement",
            "category": "Commercial",
            "status": "Awaiting Review",
            "currentStep": "approval",
            "counterparty": "Foundry Group LP",
            "owner": "Sarah Lin",
            "governingLaw": "Delaware, USA",
            "effectiveDate": "Oct 24, 2026",
            "summary": "Standard Delaware 2-year bilateral non-disclosure agreement prepared for Foundry Group partner review. Includes standard trade secret protections.",
            "riskRating": "Clean"
        },
        {
            "id": "doc-2",
            "title": "YC Post-Money SAFE (Valuation Cap: $14M)",
            "type": "SAFE Agreement",
            "category": "Corporate",
            "status": "Complete",
            "currentStep": "complete",
            "counterparty": "Foundry Angel Syndicate",
            "owner": "Sarah Lin",
            "governingLaw": "Delaware, USA",
            "effectiveDate": "Oct 20, 2026",
            "summary": "Executed $150K post-money SAFE instrument at $14M valuation cap. Funds wired and reconciled in company operating account.",
            "riskRating": "Clean"
        }
    ],
    "approvals": [
        {
            "id": "app-1",
            "department": "legal",
            "departmentLabel": "Legal Shield",
            "title": "Series Seed Mutual NDA · Foundry Group",
            "shortDescription": "Foundry GP signed bilateral agreement. Requires countersignature.",
            "timeAgo": "12m ago",
            "statusLabel": "Awaiting signature",
            "action": "Countersign NDA"
        },
        {
            "id": "app-2",
            "department": "hiring",
            "departmentLabel": "Talent Architecture",
            "title": "Aisha Khan · Staff Frontend Offer Package",
            "shortDescription": "4/4 unanimous team scorecards. Headcount burn modeled at +$14.5k/mo.",
            "timeAgo": "45m ago",
            "statusLabel": "Offer ready",
            "action": "Approve Offer Package"
        }
    ],
    "activities": [
        {
            "id": "act-1",
            "department": "legal",
            "action": "Delaware SAFE Executed",
            "shortDescription": "$150K SAFE note countersigned & vaulted.",
            "time": "12m ago"
        },
        {
            "id": "act-2",
            "department": "finance",
            "action": "Mercury Ledger Sync",
            "shortDescription": "Operating cash balance reconciled to $284,500.",
            "time": "1h ago"
        },
        {
            "id": "act-3",
            "department": "hiring",
            "action": "Final Scorecard Submitted",
            "shortDescription": "Engineering team recommended strong hire for Aisha Khan.",
            "time": "2h ago"
        }
    ]
}


class Storage:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self.state: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        if os.path.exists(STORAGE_FILE):
            try:
                with open(STORAGE_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return DEFAULT_STATE.copy()

    def _save(self):
        try:
            with open(STORAGE_FILE, "w", encoding="utf-8") as f:
                json.dump(self.state, f, indent=2)
        except Exception as e:
            print(f"Error saving storage: {e}")

    def get_state(self) -> Dict[str, Any]:
        return self.state

    def update_finance(self, cash: str, monthly_burn: str, runway: str, monthly_revenue: str):
        self.state["finance"].update({
            "cash": cash,
            "monthlyBurn": monthly_burn,
            "runway": runway,
            "monthlyRevenue": monthly_revenue,
            "lastUpdated": "Just now"
        })
        self.add_activity("finance", "Runway Snapshot Calibrated", f"Reserves: {cash} · Runway: {runway}")
        self._save()
        return self.state["finance"]

    def add_document(self, doc_data: Dict[str, Any]):
        self.state["documents"].insert(0, doc_data)
        self.add_activity("legal", f"Document Created: {doc_data.get('type')}", doc_data.get("title", ""))
        self._save()
        return doc_data

    def approve_document(self, doc_id: str):
        for doc in self.state["documents"]:
            if doc["id"] == doc_id:
                doc["status"] = "Complete"
                doc["currentStep"] = "complete"
                self.add_activity("legal", "Agreement Executed", f"Delaware verified & countersigned: {doc['title']}")
                self._save()
                return doc
        return None

    def add_role(self, role_data: Dict[str, Any]):
        self.state["roles"].insert(0, role_data)
        self.add_activity("hiring", "Role Headcount Opened", f"Opened {role_data.get('title')}")
        self._save()
        return role_data

    def add_activity(self, department: str, action: str, short_desc: str):
        new_act = {
            "id": f"act-{len(self.state['activities']) + 1}",
            "department": department,
            "action": action,
            "shortDescription": short_desc,
            "time": "Just now"
        }
        self.state["activities"].insert(0, new_act)
        self._save()
        return new_act


# Global storage singleton
db = Storage()
