"""Phase 5: a transparent personal baseline calculator (simple average)."""

from app.models import HealthRecord


def calculate_baseline(records: list[HealthRecord]):
    """Return average measurements from this patient's saved records.

    This is a learning/demo feature, not a medical reference range or diagnosis.
    """
    if not records:
        return None

    count = len(records)
    return {
        "record_count": count,
        "average_systolic_bp": round(sum(record.systolic_bp for record in records) / count, 1),
        "average_diastolic_bp": round(sum(record.diastolic_bp for record in records) / count, 1),
        "average_heart_rate": round(sum(record.heart_rate for record in records) / count, 1),
        "average_weight": round(sum(record.weight for record in records) / count, 1),
        "note": "A simple average of this synthetic patient's saved records. It is not medical advice.",
    }
