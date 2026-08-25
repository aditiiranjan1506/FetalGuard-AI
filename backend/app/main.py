"""FetalGuard AI API: Phase 5 endpoint wiring only (no risk scoring or ML)."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, SessionLocal, engine
from app.routes import health_records, patients
from app.seed_data import add_synthetic_demo_data


app = FastAPI(title="FetalGuard AI API", version="0.5.0")

# Both common Vite ports are allowed: 5173 normally, 5174 when 5173 is busy.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", "http://127.0.0.1:5173",
        "http://localhost:5174", "http://127.0.0.1:5174",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


@app.on_event("startup")
def set_up_database():
    """Create tables if needed, then add one synthetic demo profile and history."""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        add_synthetic_demo_data(db)
    finally:
        db.close()


@app.get("/api/health")
def health_check():
    return {"message": "FetalGuard AI API is running", "phase": 5}


app.include_router(patients.router)
app.include_router(health_records.router)
