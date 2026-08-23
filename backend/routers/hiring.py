"""
Router: Talent Architecture, Headcount & Candidate Scorecards
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from ..storage import db

router = APIRouter(prefix="/api/hiring", tags=["Talent & Hiring"])


class CreateRoleRequest(BaseModel):
    title: str
    department: str
    salary: str
    equity: str
    location: Optional[str] = "San Francisco, CA (Hybrid)"
    type: Optional[str] = "Full-time"


@router.get("/roles")
def get_roles():
    """
    Returns active open headcount and department bands.
    """
    state = db.get_state()
    return state["roles"]


@router.post("/roles")
def create_role(req: CreateRoleRequest):
    """
    Opens a new role calibrated against company runway.
    """
    new_role = {
        "id": f"role-{len(db.get_state()['roles']) + 1}",
        "title": req.title,
        "department": req.department,
        "salary": req.salary,
        "equity": req.equity,
        "location": req.location or "San Francisco, CA (Hybrid)",
        "type": req.type or "Full-time",
        "activeCandidates": 0,
        "status": "Open",
        "hiringLead": db.get_state()["founder"]["name"]
    }
    db.add_role(new_role)
    return {"status": "success", "data": new_role}


@router.get("/candidates")
def get_candidates():
    """
    Returns active candidate pipeline and scorecards.
    """
    state = db.get_state()
    return state["candidates"]
