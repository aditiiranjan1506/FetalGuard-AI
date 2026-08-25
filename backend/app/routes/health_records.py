from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import HealthRecord, Patient
from app.schemas import CheckInResponse, HealthRecordInput, HealthRecordResponse
from app.services.anomaly import calculate_anomaly_score
from app.services.baseline import calculate_baseline
from app.services.explanation import build_explanation


router = APIRouter(prefix="/api", tags=["health records"])


def ensure_patient_exists(patient_id: int, db: Session):
    if db.get(Patient, patient_id) is None:
        raise HTTPException(status_code=404, detail="Demo patient not found")


@router.get("/health-records/{patient_id}", response_model=list[HealthRecordResponse])
def list_health_records(patient_id: int, db: Session = Depends(get_db)):
    ensure_patient_exists(patient_id, db)
    return db.scalars(
        select(HealthRecord).where(HealthRecord.patient_id == patient_id).order_by(HealthRecord.date)
    ).all()


@router.post("/health-records/{patient_id}", response_model=CheckInResponse)
def create_health_record(patient_id: int, record: HealthRecordInput, db: Session = Depends(get_db)):
    ensure_patient_exists(patient_id, db)
    # Calculate against history *before* adding the new record.
    previous_records = db.scalars(
        select(HealthRecord).where(HealthRecord.patient_id == patient_id).order_by(HealthRecord.date)
    ).all()
    baseline = calculate_baseline(previous_records)
    saved_record = HealthRecord(patient_id=patient_id, date=date.today(), **record.model_dump())
    db.add(saved_record)
    db.commit()
    db.refresh(saved_record)
    explanation = build_explanation(calculate_anomaly_score(saved_record, baseline), saved_record.symptoms)
    return {"record": saved_record, **explanation}


@router.get("/dashboard/{patient_id}")
def get_dashboard(patient_id: int, db: Session = Depends(get_db)):
    patient = db.get(Patient, patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="Demo patient not found")
    records = db.scalars(
        select(HealthRecord).where(HealthRecord.patient_id == patient_id).order_by(HealthRecord.date)
    ).all()
    latest = records[-1] if records else None
    latest_explanation = None
    if latest:
        # Use earlier records as the comparison history when possible.
        comparison_history = records[:-1] or records
        latest_explanation = build_explanation(
            calculate_anomaly_score(latest, calculate_baseline(comparison_history)), latest.symptoms
        )
    return {
        "patient": patient,
        "latest_record": latest,
        "baseline": calculate_baseline(records),
        "latest_explanation": latest_explanation,
    }
