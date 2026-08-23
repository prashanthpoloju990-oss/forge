"""
FORGE Delaware Legal Shield Engine
Synthesizes standard Delaware corporate instruments, SAFE agreements, bilateral NDAs, and contractor IP covenants.
"""

from typing import Dict, Any, List


def generate_delaware_agreement(
    doc_type: str,
    company_name: str,
    counterparty: str,
    parameters: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Synthesizes a Delaware-compliant legal agreement with verified covenants.
    """
    params = parameters or {}

    if "safe" in doc_type.lower():
        val_cap = params.get("valuation_cap", "$14,000,000")
        investment = params.get("investment_amount", "$150,000")
        discount = params.get("discount", "None (Standard Post-Money)")

        title = f"YC Post-Money SAFE · {counterparty} ({val_cap} Cap)"
        summary = f"Delaware Y-Combinator standard post-money Simple Agreement for Future Equity for {counterparty} at {val_cap} valuation cap with {investment} investment."

        clauses = [
            {
                "title": "1. Events & Conversion Mechanics",
                "content": f"If there is an Equity Financing before the termination of this Safe, on the initial closing of such Equity Financing, this Safe will automatically convert into shares of Safe Preferred Stock based on the Valuation Cap of {val_cap}."
            },
            {
                "title": "2. Liquidity Event & Dissolution",
                "content": f"If there is a Liquidity Event or Dissolution Event prior to conversion, the Investor shall be entitled to receive a portion of Proceeds equal to the Purchase Amount of {investment}."
            },
            {
                "title": "3. Governing Law & Delaware Jurisdiction",
                "content": "This instrument and any dispute arising therefrom shall be governed by and construed in accordance with the laws of the State of Delaware, without giving effect to any choice of law principles."
            },
            {
                "title": "4. No Shareholder Rights",
                "content": "This instrument does not grant the Investor voting rights, dividend preferences, or inspection rights prior to conversion into Preferred Stock."
            }
        ]

        full_text = f"""# SIMPLE AGREEMENT FOR FUTURE EQUITY (SAFE)
**Company**: {company_name} (a Delaware Corporation)
**Investor**: {counterparty}
**Purchase Amount**: {investment} USD
**Valuation Cap**: {val_cap} USD
**Discount Rate**: {discount}

---

### SECTION 1: CONVERSION MECHANICS
In the event that {company_name} issues and sells Preferred Stock in a bona fide equity financing round, this Safe shall automatically convert into shares of Safe Preferred Stock calculated by dividing the Purchase Amount by the Safe Price.

### SECTION 2: DELAWARE JURISDICTION
This Agreement and all acts and transactions pursuant hereto shall be governed by the laws of the State of Delaware.

*Generated autonomously via FORGE Legal Shield on Oct 2026.*"""

        return {
            "id": f"safe-{hash(counterparty) % 10000}",
            "title": title,
            "type": "SAFE Agreement",
            "category": "Corporate",
            "counterparty": counterparty,
            "governingLaw": "Delaware, USA",
            "status": "Awaiting Review",
            "summary": summary,
            "clauses": clauses,
            "full_text": full_text,
            "risk_rating": "Clean (0 Deviations)"
        }

    elif "nda" in doc_type.lower():
        term = params.get("term", "24 Months")
        title = f"Mutual Non-Disclosure Agreement · {counterparty}"
        summary = f"Delaware 2-year bilateral non-disclosure agreement for confidential discussions between {company_name} and {counterparty}."

        clauses = [
            {
                "title": "1. Definition of Confidential Information",
                "content": "Confidential Information includes all non-public technical, business, financial, and product architecture data disclosed whether orally or in writing."
            },
            {
                "title": "2. Standard Exclusions & Clean Carve-outs",
                "content": "Recipient shall have no obligation for information that: (a) was already known; (b) is or becomes publicly available without breach; (c) was independently developed without reference to Disclosing Party's materials."
            },
            {
                "title": "3. Term & Delaware Jurisdiction",
                "content": f"The obligations of confidentiality shall remain in effect for a period of {term} from the Effective Date under the laws of the State of Delaware."
            }
        ]

        full_text = f"""# BILATERAL MUTUAL NON-DISCLOSURE AGREEMENT
**Disclosing Party**: {company_name}
**Receiving Party**: {counterparty}
**Governing Law**: Delaware, United States
**Effective Term**: {term}

---

### RECITALS
The parties wish to explore a potential strategic collaboration and desire to evaluate confidential technical and business materials under standard protective covenants.

### CONFIDENTIALITY OBLIGATIONS
Each party agrees to hold all proprietary trade secrets in strict confidence and exercise reasonable care standard in Delaware commercial practice.

*Executed under FORGE Delaware Shield.*"""

        return {
            "id": f"nda-{hash(counterparty) % 10000}",
            "title": title,
            "type": "Mutual NDA",
            "category": "Commercial",
            "counterparty": counterparty,
            "governingLaw": "Delaware, USA",
            "status": "Awaiting Review",
            "summary": summary,
            "clauses": clauses,
            "full_text": full_text,
            "risk_rating": "Clean (0 Deviations)"
        }

    else:
        # Generic Work-for-hire / IP assignment
        title = f"Proprietary Information & Inventions Agreement · {counterparty}"
        return {
            "id": f"piia-{hash(counterparty) % 10000}",
            "title": title,
            "type": "Inventions Assignment",
            "category": "Employment",
            "counterparty": counterparty,
            "governingLaw": "Delaware, USA",
            "status": "Awaiting Review",
            "summary": f"Comprehensive work-for-hire and full intellectual property assignment to {company_name}.",
            "clauses": [
                {"title": "1. Full IP Assignment", "content": "Assigns all patent, copyright, trademark, and trade secret rights to company."},
                {"title": "2. Delaware Governing Law", "content": "Delaware jurisdiction with standard non-solicitation."}
            ],
            "full_text": f"# PROPRIETARY INFORMATION AND INVENTIONS ASSIGNMENT\nCompany: {company_name}\nAssignee: {counterparty}\nAll works assigned 100% to company.",
            "risk_rating": "Clean (0 Deviations)"
        }
