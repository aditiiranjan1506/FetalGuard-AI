"""Phase 7: deliberately small, transparent symptom keyword matching."""


KEYWORDS = {
    "headache": "The symptom description mentions headache.",
    "dizzy": "The symptom description mentions dizziness.",
    "dizziness": "The symptom description mentions dizziness.",
    "swelling": "The symptom description mentions swelling.",
    "blurred vision": "The symptom description mentions blurred vision.",
    "pain": "The symptom description mentions pain.",
}


def find_symptom_reasons(symptoms: str):
    """Return neutral text matches; this does not interpret or diagnose symptoms."""
    lower_case_text = symptoms.lower()
    found_reasons = []
    for keyword, reason in KEYWORDS.items():
        if keyword in lower_case_text and reason not in found_reasons:
            found_reasons.append(reason)
    return found_reasons
