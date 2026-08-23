"""
Router: Delaware Legal Shield & Document Governance
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from ..services.delaware_legal_engine import generate_delaware_agreement
from ..storage import db

router = APIRouter(prefix="/api/legal", tags=["Delaware Legal Shield"])


class GenerateDocumentRequest(BaseModel):
    doc_type: str
    counterparty: str
    company_name: Optional[str] = "Acme Inc."
    parameters: Optional[Dict[str, Any]] = None


class ApproveDocumentRequest(BaseModel):
    document_id: str
    notes: Optional[str] = None


@router.get("/documents")
def get_documents():
    """
    Returns all company contracts, SAFE notes, and NDAs.
    """
    state = db.get_state()
    return state["documents"]


@router.post("/generate")
def generate_contract(req: GenerateDocumentRequest):
    """
    Synthesizes a standardized Delaware corporate document.
    """
    doc = generate_delaware_agreement(
        doc_type=req.doc_type,
        company_name=req.company_name or "Acme Inc.",
        counterparty=req.counterparty,
        parameters=req.parameters
    )
    # Persist into company vault
    db.add_document(doc)
    return {"status": "success", "data": doc}


@router.post("/approve")
def approve_contract(req: ApproveDocumentRequest):
    """
    Countersigns and executes a legal agreement under Delaware law.
    """
    doc = db.approve_document(req.document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"status": "success", "message": f"Executed {doc['title']}", "data": doc}
