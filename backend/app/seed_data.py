"""Phase 3: safe, clearly synthetic starting records for a demo patient."""

from datetime import date, timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import HealthRecord, Patient


def add_synthetic_demo_data(db: Session):
    """Add data only to an empty database, so server restarts do not duplicate it."""
    if db.scalar(select(Patient.id).limit(1)):
        return

    patient = Patient(name="Maya Patel", age=29, pregnancy_week=24)
    db.add(patient)
    db.flush()  # Gives the new patient an id before we create her records.

    # These values are invented for UI development only, not medical guidance.
    demo_values = [
        (20, 114, 72, 78, 60.4, "Feeling well."),
        (21, 115, 73, 79, 60.7, ""),
        (22, 116, 74, 80, 61.1, "Mild tiredness after work."),
        (23, 117, 75, 81, 61.5, ""),
        (24, 118, 76, 82, 62.0, "Feeling well today."),
    ]
    start_date = date.today() - timedelta(days=(len(demo_values) - 1) * 7)

    for index, (week, systolic, diastolic, heart_rate, weight, symptoms) in enumerate(demo_values):
        db.add(HealthRecord(
            patient_id=patient.id,
            date=start_date + timedelta(days=index * 7),
            pregnancy_week=week,
            systolic_bp=systolic,
            diastolic_bp=diastolic,
            heart_rate=heart_rate,
            weight=weight,
            symptoms=symptoms,
        ))
    db.commit()
