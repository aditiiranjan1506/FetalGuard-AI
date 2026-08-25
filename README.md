# FetalGuard AI — Through Phase 8

A beginner-friendly, synthetic-data-only hackathon prototype. React sends a Daily Check-In to FastAPI; FastAPI saves it in SQLite and returns JSON. The app shows trends, a simple personal baseline, transparent rule-based change scoring, symptom keyword matches, and a safe explanation UI.

## Run the backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be at `http://127.0.0.1:8000`. Visit `/docs` to try endpoints manually.

## Run the frontend

In a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL Vite prints (normally `http://localhost:5173`).

## Phase 1 endpoints

- `GET /api/health`
- `GET /api/patients/{patient_id}`
- `GET /api/health-records/{patient_id}`
- `GET /api/dashboard/{patient_id}`
- `POST /api/health-records/{patient_id}`

Included through Phase 8: SQLite, SQLAlchemy, synthetic seed data, health-record retrieval, Recharts trends, a transparent simple-average baseline, simple change scoring, symptom keyword matching, and an explanation/alert UI. Not included: machine learning or Isolation Forest.

## Safety note

This uses synthetic demo data only. Its scoring and keyword matching are simple software demonstrations, not clinical rules, medical advice, or diagnosis.
