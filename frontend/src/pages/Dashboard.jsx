import { useEffect, useState } from "react";
import { getDashboard } from "../services/api";

export default function Dashboard() {
  const [dashboard, setDashboard] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    getDashboard(1).then(setDashboard).catch((requestError) => setError(requestError.message));
  }, []);

  if (error) return <section className="page"><p className="message error">{error}</p></section>;
  if (!dashboard) return <section className="page"><p>Loading the synthetic demo profile…</p></section>;

  const { patient, latest_record: latest, baseline, latest_explanation: latestExplanation } = dashboard;
  return (
    <section className="page">
      <p className="eyebrow">DASHBOARD</p>
      <h2>Welcome, {patient.name}</h2>
      <p className="muted">Local SQLite data for a clearly labelled synthetic demo patient.</p>

      <div className="card-grid">
        <article className="card"><span>Pregnancy week</span><strong>{latest.pregnancy_week}</strong></article>
        <article className="card"><span>Latest blood pressure</span><strong>{latest.systolic_bp} / {latest.diastolic_bp}</strong></article>
        <article className="card"><span>Latest heart rate</span><strong>{latest.heart_rate} bpm</strong></article>
        <article className="card"><span>Latest weight</span><strong>{latest.weight} kg</strong></article>
      </div>

      <article className="status-card">
        <h3>Personal baseline (Phase 5)</h3>
        <p>Based on {baseline.record_count} saved synthetic check-ins:</p>
        <p className="baseline-values">
          BP {baseline.average_systolic_bp} / {baseline.average_diastolic_bp} · Heart rate {baseline.average_heart_rate} bpm · Weight {baseline.average_weight} kg
        </p>
        <p className="muted">{baseline.note}</p>
      </article>
      {latestExplanation && (
        <article className={`alert-card ${latestExplanation.status}`}>
          <p className="eyebrow">LATEST PROTOTYPE STATUS — {latestExplanation.status.toUpperCase()}</p>
          <h3>Latest change score: {latestExplanation.risk_score}/100</h3>
          <ul>{latestExplanation.reasons.map((reason) => <li key={reason}>{reason}</li>)}</ul>
          <p><strong>Next step:</strong> {latestExplanation.recommendation}</p>
        </article>
      )}
      <p className="disclaimer">FetalGuard AI is a hackathon prototype, not a medical diagnostic tool.</p>
    </section>
  );
}
