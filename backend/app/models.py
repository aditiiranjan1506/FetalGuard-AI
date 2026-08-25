"""Phase 2: Python descriptions of the two SQLite tables."""

from datetime import date

from sqlalchemy import Date, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)
    pregnancy_week: Mapped[int] = mapped_column(Integer)
    health_records: Mapped[list["HealthRecord"]] = relationship(back_populates="patient")


class HealthRecord(Base):
    __tablename__ = "health_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"))
    date: Mapped[date] = mapped_column(Date)
    pregnancy_week: Mapped[int] = mapped_column(Integer)
    systolic_bp: Mapped[int] = mapped_column(Integer)
    diastolic_bp: Mapped[int] = mapped_column(Integer)
    heart_rate: Mapped[int] = mapped_column(Integer)
    weight: Mapped[float] = mapped_column(Float)
    symptoms: Mapped[str] = mapped_column(Text, default="")
    patient: Mapped[Patient] = relationship(back_populates="health_records")
