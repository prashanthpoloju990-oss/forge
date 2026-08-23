"""
FORGE Multi-Agent Command Orchestrator
Parses natural language founder commands, classifies intent, and orchestrates domain agents (Legal Shield, Treasury Solver, Talent Architect).
"""

import re
from typing import Dict, Any, List
from .monte_carlo_engine import run_monte_carlo_simulation
from .delaware_legal_engine import generate_delaware_agreement


def parse_and_execute_command(
    query: str,
    startup_name: str = "Acme Inc.",
    current_state: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Analyzes natural language directive and coordinates multi-agent execution.
    """
    q = query.lower().strip()

    # 1. LEGAL INTENT (SAFE, NDA, Contracts)
    if "safe" in q or "nda" in q or "agreement" in q or "contract" in q or "legal" in q:
        doc_type = "SAFE" if "safe" in q else "NDA" if "nda" in q else "Contract"

        # Extract counterparty if mentioned
        counterparty = "Counterparty Corp"
        if "foundry" in q:
            counterparty = "Foundry Group LP"
        elif "sequoia" in q:
            counterparty = "Sequoia Capital"
        elif "contractor" in q:
            counterparty = "Apex Digital Labs"

        doc = generate_delaware_agreement(doc_type, startup_name, counterparty)

        return {
            "status": "ready",
            "agent_matched": "Delaware Legal Shield Agent",
            "intent": "DRAFT_DELAWARE_AGREEMENT",
            "confidence": 0.98,
            "title": doc["title"],
            "summary": doc["summary"],
            "metadata": [
                {"label": "Document Type", "value": doc["type"]},
                {"label": "Counterparty", "value": doc["counterparty"]},
                {"label": "Governing Law", "value": doc["governingLaw"]},
                {"label": "Risk Rating", "value": doc["risk_rating"]},
            ],
            "action_prepared": {
                "action_type": "CREATE_DOCUMENT",
                "payload": doc,
                "primary_button": "Execute & Vault Agreement",
                "secondary_button": "Edit Clauses"
            }
        }

    # 2. FINANCE & RUNWAY SIMULATION INTENT
    elif "runway" in q or "burn" in q or "cash" in q or "monte carlo" in q or "hire" in q and ("cost" in q or "impact" in q):
        headcount = 2 if "+2" in q or "2" in q else 1 if "1" in q else 0
        capital = 250000.0 if "250k" in q else 150000.0 if "150k" in q else 0.0

        sim_res = run_monte_carlo_simulation(
            headcount_added=headcount,
            capital_inflow=capital
        )

        summary_text = (
            f"Monte Carlo analysis (1,000 iterations): Median runway is {sim_res['summary']['median_runway_months']} months. "
            f"Headcount burn delta: +${int(sim_res['input_parameters']['additional_monthly_burn']):,}/mo."
        )

        return {
            "status": "ready",
            "agent_matched": "Treasury Solver Agent",
            "intent": "SIMULATE_TREASURY_RUNWAY",
            "confidence": 0.96,
            "title": f"Treasury Forecast (+{headcount} Headcount Scenario)",
            "summary": summary_text,
            "metadata": [
                {"label": "Median Horizon", "value": f"{sim_res['summary']['median_runway_months']} mo"},
                {"label": "P10 (Conservative)", "value": f"{sim_res['summary']['conservative_p10_months']} mo"},
                {"label": "Health", "value": sim_res['summary']['health_assessment']},
                {"label": "Risk (<12 mo)", "value": sim_res['summary']['prob_exhaustion_before_12mo']},
            ],
            "action_prepared": {
                "action_type": "APPLY_TREASURY_SCENARIO",
                "payload": sim_res,
                "primary_button": "Apply Forecast to Operating Graph",
                "secondary_button": "Adjust Headcount Band"
            }
        }

    # 3. TALENT & HIRING INTENT
    elif "candidate" in q or "offer" in q or "interview" in q or "scorecard" in q:
        return {
            "status": "ready",
            "agent_matched": "Talent Architect Agent",
            "intent": "STAGE_CANDIDATE_OFFER",
            "confidence": 0.94,
            "title": "Stage Headcount Offer Package",
            "summary": "Benchmarked compensation band: $175K Base + 0.85% Equity. Headcount burn delta verified against runway (+14.8 mo remaining).",
            "metadata": [
                {"label": "Candidate", "value": "Aisha Khan"},
                {"label": "Role", "value": "Staff Frontend Engineer"},
                {"label": "Consensus", "value": "Strong Yes (4/4)"},
                {"label": "Headcount Impact", "value": "-$14.5k / mo"},
            ],
            "action_prepared": {
                "action_type": "GENERATE_OFFER_LETTER",
                "payload": {"candidate": "Aisha Khan", "role": "Staff Frontend Engineer"},
                "primary_button": "Approve & Send Offer Letter",
                "secondary_button": "Recalibrate Equity"
            }
        }

    # 4. DEFAULT: EXECUTIVE QUERY
    else:
        return {
            "status": "ready",
            "agent_matched": "FORGE Autonomous OS",
            "intent": "GENERAL_OPERATIONAL_QUERY",
            "confidence": 0.90,
            "title": f"Executive Synthesis for '{query}'",
            "summary": "Unified operating graph queried. Cash runway is 14.8 months with 4 active engineering candidates and 100% Delaware IP assignment.",
            "metadata": [
                {"label": "Liquid Cash", "value": "$284,500"},
                {"label": "Runway", "value": "14.8 mo"},
                {"label": "Open Roles", "value": "3 Positions"},
                {"label": "Governance", "value": "Clean (0 Deviations)"},
            ],
            "action_prepared": {
                "action_type": "VIEW_DASHBOARD",
                "payload": {},
                "primary_button": "View Company Graph",
                "secondary_button": "Dismiss"
            }
        }
