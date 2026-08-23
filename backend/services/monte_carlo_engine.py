"""
FORGE Monte Carlo Treasury & Runway Simulation Engine
Runs 1,000 probabilistic simulations to project cash horizons, burn acceleration, and default probability.
"""

import numpy as np
from typing import Dict, Any, List


def run_monte_carlo_simulation(
    starting_cash: float = 284500.0,
    base_monthly_burn: float = 19200.0,
    base_monthly_revenue: float = 8400.0,
    revenue_growth_mean: float = 0.08,
    revenue_growth_std: float = 0.04,
    burn_growth_std: float = 0.03,
    headcount_added: int = 0,
    salary_per_headcount: float = 14500.0,
    capital_inflow: float = 0.0,
    capital_inflow_month: int = 1,
    months: int = 24,
    iterations: int = 1000
) -> Dict[str, Any]:
    """
    Executes a 1,000-run Monte Carlo simulation for cash reserves.
    """
    np.random.seed(42)  # Deterministic seed for reproducible executive models

    # Cash matrix: shape (iterations, months + 1)
    cash_trajectories = np.zeros((iterations, months + 1))
    cash_trajectories[:, 0] = starting_cash

    runway_months = []

    # Additional monthly cost from staged headcount
    additional_monthly_burn = headcount_added * salary_per_headcount

    for i in range(iterations):
        current_cash = starting_cash
        current_burn = base_monthly_burn + additional_monthly_burn
        current_rev = base_monthly_revenue
        depleted_month = None

        for m in range(1, months + 1):
            # Apply capital injection if specified for this month
            if m == capital_inflow_month and capital_inflow > 0:
                current_cash += capital_inflow

            # Stochastic monthly revenue growth
            growth = np.random.normal(revenue_growth_mean, revenue_growth_std)
            current_rev = max(0, current_rev * (1 + growth))

            # Stochastic burn fluctuation (e.g. AWS surges, legal fees)
            burn_shock = np.random.normal(0, burn_growth_std)
            effective_burn = max(5000, current_burn * (1 + burn_shock))

            # Net cash delta for the month
            net_delta = current_rev - effective_burn
            current_cash += net_delta
            cash_trajectories[i, m] = max(0, current_cash)

            if current_cash <= 0 and depleted_month is None:
                depleted_month = m

        if depleted_month is None:
            runway_months.append(months)
        else:
            runway_months.append(depleted_month)

    runway_arr = np.array(runway_months)

    # Statistical percentiles
    p10_runway = float(np.percentile(runway_arr, 10))
    p50_runway = float(np.percentile(runway_arr, 50))
    p90_runway = float(np.percentile(runway_arr, 90))

    # Cash trajectory percentiles per month
    p10_cash = np.percentile(cash_trajectories, 10, axis=0).tolist()
    p50_cash = np.percentile(cash_trajectories, 50, axis=0).tolist()
    p90_cash = np.percentile(cash_trajectories, 90, axis=0).tolist()

    # Risk metrics
    prob_exhaustion_12m = float(np.mean(runway_arr < 12) * 100)
    prob_exhaustion_18m = float(np.mean(runway_arr < 18) * 100)

    month_labels = [f"Month {m}" for m in range(months + 1)]

    return {
        "status": "success",
        "iterations": iterations,
        "input_parameters": {
            "starting_cash": starting_cash,
            "base_monthly_burn": base_monthly_burn,
            "headcount_added": headcount_added,
            "additional_monthly_burn": additional_monthly_burn,
            "capital_inflow": capital_inflow,
        },
        "summary": {
            "median_runway_months": round(p50_runway, 1),
            "conservative_p10_months": round(p10_runway, 1),
            "optimistic_p90_months": round(p90_runway, 1),
            "prob_exhaustion_before_12mo": f"{round(prob_exhaustion_12m, 1)}%",
            "prob_exhaustion_before_18mo": f"{round(prob_exhaustion_18m, 1)}%",
            "health_assessment": "Optimal" if p50_runway >= 14 else "Caution" if p50_runway >= 8 else "Critical"
        },
        "trajectories": {
            "labels": month_labels,
            "p10_conservative": [round(val, 2) for val in p10_cash],
            "p50_median": [round(val, 2) for val in p50_cash],
            "p90_optimistic": [round(val, 2) for val in p90_cash]
        }
    }
