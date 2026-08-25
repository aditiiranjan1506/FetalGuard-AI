# FetalGuard AI 

FetalGuard AI is a small HealthTech hackathon prototype for monitoring changes in pregnancy-related health data over time.

The idea is simple: instead of looking at a single health measurement in isolation, FetalGuard keeps track of previous measurements and creates a basic personal baseline. New check-ins are compared with that baseline to highlight noticeable changes.

The prototype also looks for a few symptoms entered in normal text and explains why a change was flagged.

> **Important:** FetalGuard AI is an educational prototype, not a medical device. It does not diagnose diseases, provide medical advice, or replace a healthcare professional.

---

## What it does

A user can submit a daily check-in containing:

- Pregnancy week
- Systolic blood pressure
- Diastolic blood pressure
- Heart rate
- Weight
- Symptoms in plain text

The information is stored locally in SQLite.

FetalGuard then uses the available history to:

- Show recent health information
- Display blood pressure, heart-rate, and weight trends
- Calculate a simple personal baseline
- Compare new measurements with that baseline
- Generate a transparent change score
- Detect a small set of symptom keywords
- Explain the reasons behind a flagged change

All data used in this repository is synthetic demo data.

---

## How it works

The application has two main parts: a React frontend and a Python/FastAPI backend.

```text
                    FetalGuard AI

                         User
                          │
                          ▼
                 React + Vite
                    Frontend
                          │
                     HTTP / JSON
                          │
                          ▼
                    FastAPI
                    Backend
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
           SQLite              Analysis Logic
              │                       │
              └───────────┬───────────┘
                          ▼
                    JSON response
                          │
                          ▼
                    React UI
