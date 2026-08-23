"""
Router: Treasury, Cash Ledger & Monte Carlo Simulation
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from ..services.monte_carlo_engine import run_monte_carlo_simulation
from ..storage import db

router = APIRouter(prefix="/api/finance", tags=["Finance & Treasury"])


class UpdateSnapshotRequest(BaseModel):
    cash: str
    monthlyBurn: str
    runway: str
    monthlyRevenue: str


class SimulateRequest(BaseModel):
    starting_cash: Optional[float] = 284500.0
    base_monthly_burn: Optional[float] = 19200.0
    base_monthly_revenue: Optional[float] = 8400.0
    headcount_added: Optional[int] = 0
    salary_per_headcount: Optional[float] = 14500.0
    capital_inflow: Optional[float] = 0.0
    months: Optional[int] = 24


@router.get("/snapshot")
def get_financial_snapshot():
    """
    Returns the live reconciled financial snapshot.
    """
    state = db.get_state()
    return state["finance"]


@router.post("/snapshot")
def update_financial_snapshot(req: UpdateSnapshotRequest):
    """
    Calibrates treasury reserves and updates company runway.
    """
    updated = db.update_finance(
        cash=req.cash,
        monthly_burn=req.monthlyBurn,
        runway=req.runway,
        monthly_revenue=req.monthlyRevenue
    )
    return {"status": "success", "data": updated}


@router.post("/simulate")
def simulate_runway_scenarios(req: SimulateRequest):
    """
    Runs a 1,000-iteration Monte Carlo cash simulation.
    """
    result = run_monte_carlo_simulation(
        starting_cash=req.starting_cash or 284500.0,
        base_monthly_burn=req.base_monthly_burn or 19200.0,
        base_monthly_revenue=req.base_monthly_revenue or 8400.0,
        headcount_added=req.headcount_added or 0,
        salary_per_headcount=req.salary_per_headcount or 14500.0,
        capital_inflow=req.capital_inflow or 0.0,
        months=req.months or 24
    )
    return result
