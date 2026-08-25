"""Phase 6: a simple, explainable change score (not a medical diagnosis)."""


def calculate_anomaly_score(record, baseline):
    """Compare one record with a patient's simple-average baseline.

    The points and thresholds are intentionally easy to read for this hackathon
    prototype. They are not clinical rules and must never be used for diagnosis.
    """
    if baseline is None:
        return {"score": 0, "measurement_reasons": ["Not enough saved history to compare yet."]}

    score = 0
    reasons = []
    if record.systolic_bp >= baseline["average_systolic_bp"] + 10:
        score += 35
        reasons.append("Systolic blood-pressure measurement is noticeably above this personal average.")
    if record.diastolic_bp >= baseline["average_diastolic_bp"] + 8:
        score += 25
        reasons.append("Diastolic blood-pressure measurement is noticeably above this personal average.")
    if record.heart_rate >= baseline["average_heart_rate"] + 12:
        score += 25
        reasons.append("Heart-rate measurement is noticeably above this personal average.")
    if record.weight >= baseline["average_weight"] + 2:
        score += 15
        reasons.append("Weight is noticeably above this personal average.")

    return {"score": min(score, 100), "measurement_reasons": reasons}


def status_from_score(score):
    if score >= 50:
        return "attention"
    if score >= 20:
        return "watch"
    return "typical"
