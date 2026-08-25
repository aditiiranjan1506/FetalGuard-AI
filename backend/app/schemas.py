"""The JSON shapes accepted and returned by the API."""

from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class HealthRecordInput(BaseModel):
    pregnancy_week: int = Field(ge=1, le=45)
    systolic_bp: int = Field(ge=1)
    diastolic_bp: int = Field(ge=1)
    heart_rate: int = Field(ge=1)
    weight: float = Field(gt=0)
    symptoms: str = ""


class HealthRecordResponse(HealthRecordInput):
    model_config = ConfigDict(from_attributes=True)
    id: int
    patient_id: int
    date: date


class PatientResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    age: int
    pregnancy_week: int


class CheckInResponse(BaseModel):
    """The saved record plus its Phase 6–8 prototype explanation."""

    record: HealthRecordResponse
    status: str
    risk_score: int
    reasons: list[str]
    recommendation: str
