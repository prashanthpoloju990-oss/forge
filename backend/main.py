"""
FORGE Autonomous Operating System - FastAPI Backend
Main entrypoint and API router configuration.
"""

from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from .routers import command, finance, legal, hiring, investor
from .storage import db

app = FastAPI(
    title="FORGE Autonomous Founder Operating System API",
    description="Backend API powering Monte Carlo runway simulation, Delaware legal synthesis, talent pipeline calibration, and ⌘K Command OS.",
    version="1.0.0"
)

# Root endpoint redirects directly to interactive Swagger docs
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

# CORS Middleware (allows Vite frontend on port 5173 / localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Domain Routers
app.include_router(command.router)
app.include_router(finance.router)
app.include_router(legal.router)
app.include_router(hiring.router)
app.include_router(investor.router)


@app.get("/api/health")
def health_check():
    """
    Health check and operational graph heartbeat.
    """
    return {
        "status": "healthy",
        "service": "FORGE OS Engine",
        "version": "1.0.0-GA",
        "timestamp": datetime.now().isoformat(),
        "graph_state": {
            "startup": db.get_state()["startup"]["name"],
            "reserves": db.get_state()["finance"]["cash"],
            "open_roles": len(db.get_state()["roles"]),
            "vaulted_docs": len(db.get_state()["documents"])
        }
    }


@app.get("/api/graph")
def get_full_graph():
    """
    Returns the complete unified operating graph.
    """
    return db.get_state()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
