import { useState } from "react";
import { submitHealthRecord } from "../services/api";

const initialForm = {
  pregnancy_week: 24,
  systolic_bp: 118,
  diastolic_bp: 76,
  heart_rate: 82,
  weight: 62,
  symptoms: "",
};

export default function DailyCheckIn() {
  const [form, setForm] = useState(initialForm);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  function updateField(event) {
    const { name, value } = event.target;
    setForm((previous) => ({ ...previous, [name]: name === "symptoms" ? value : Number(value) }));
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setIsSubmitting(true);
    setError("");
    setResult(null);

    try {
      // `form` becomes JSON in api.js, then FastAPI validates it.
      const serverResponse = await submitHealthRecord(1, form);
      setResult(serverResponse);
    } catch (requestError) {
      setError(requestError.message);
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <section className="page">
      <p className="eyebrow">DAILY CHECK-IN</p>
      <h2>Share today’s demo measurements</h2>
      <form className="check-in-form" onSubmit={handleSubmit}>
        <label>Pregnancy week<input name="pregnancy_week" type="number" min="1" value={form.pregnancy_week} onChange={updateField} required /></label>
        <label>Systolic blood pressure<input name="systolic_bp" type="number" value={form.systolic_bp} onChange={updateField} required /></label>
        <label>Diastolic blood pressure<input name="diastolic_bp" type="number" value={form.diastolic_bp} onChange={updateField} required /></label>
        <label>Heart rate<input name="heart_rate" type="number" value={form.heart_rate} onChange={updateField} required /></label>
        <label>Weight (kg)<input name="weight" type="number" step="0.1" value={form.weight} onChange={updateField} required /></label>
        <label className="full-width">Symptoms<textarea name="symptoms" value={form.symptoms} onChange={updateField} placeholder="Example: I felt tired today." /></label>
        <button className="submit-button" disabled={isSubmitting}>{isSubmitting ? "Sending..." : "Submit Check-In"}</button>
      </form>

      {error && <p className="message error">{error}</p>}
      {result && (
        <section className={`alert-card ${result.status}`}>
          <p className="eyebrow">CHECK-IN SAVED — {result.status.toUpperCase()}</p>
          <h3>Prototype change score: {result.risk_score}/100</h3>
          <p>Why this was shown:</p>
          <ul>{result.reasons.map((reason) => <li key={reason}>{reason}</li>)}</ul>
          <p><strong>Next step:</strong> {result.recommendation}</p>
          <p className="muted">Saved record #{result.record.id}. This is not a diagnosis.</p>
        </section>
      )}
      <p className="disclaimer">Synthetic data only. This prototype does not provide medical advice or diagnosis.</p>
    </section>
  );
}
