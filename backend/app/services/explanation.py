"""Phase 8: turn simple scoring outputs into a safe, clear explanation."""

from .anomaly import status_from_score
from .symptoms import find_symptom_reasons


def build_explanation(score_result, symptoms: str):
    """Create non-diagnostic UI text from the Phase 6 and 7 outputs."""
    symptom_reasons = find_symptom_reasons(symptoms)
    reasons = score_result["measurement_reasons"] + symptom_reasons
    score = score_result["score"]
    status = status_from_score(score)

    if not reasons:
        reasons = ["No notable changes were found by this prototype's simple comparison."]

    if status == "attention":
        recommendation = "Consider discussing these recorded changes with a healthcare professional."
    elif status == "watch":
        recommendation = "Keep tracking changes and consider discussing concerns with a healthcare professional."
    else:
        recommendation = "Continue routine tracking. This prototype does not provide medical advice."

    return {
        "status": status,
        "risk_score": score,
        "reasons": reasons,
        "recommendation": recommendation,
    }
