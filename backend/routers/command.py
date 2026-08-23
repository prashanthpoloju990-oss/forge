"""
Router: ⌘K Command OS & Natural Language Intent Execution
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from ..services.agent_orchestrator import parse_and_execute_command
from ..storage import db

router = APIRouter(prefix="/api/command", tags=["Command OS"])


class CommandRequest(BaseModel):
    query: str
    startup_name: Optional[str] = "Acme Inc."


class ExecuteActionRequest(BaseModel):
    action_type: str
    payload: Dict[str, Any]


@router.post("")
def process_command(req: CommandRequest):
    """
    Parses natural language founder directive and orchestrates domain agents.
    """
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    state = db.get_state()
    res = parse_and_execute_command(req.query, req.startup_name or state["startup"]["name"], state)
    return res


@router.post("/execute")
def execute_action(req: ExecuteActionRequest):
    """
    Applies the prepared multi-agent proposal into the live company graph.
    """
    if req.action_type == "CREATE_DOCUMENT":
        doc = db.add_document(req.payload)
        return {"status": "success", "message": f"Created & staged document: {doc.get('title')}", "data": doc}

    elif req.action_type == "APPLY_TREASURY_SCENARIO":
        db.add_activity("finance", "Forecast Applied", "Applied Monte Carlo runway projection to operating graph.")
        return {"status": "success", "message": "Treasury forecast updated in operating graph."}

    return {"status": "success", "message": "Action executed successfully."}
