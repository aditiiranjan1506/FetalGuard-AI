import { useEffect, useState } from "react";
import HealthTrends from "../components/HealthTrends";
import { getHealthRecords } from "../services/api";

export default function HealthTrendsPage() {
  const [records, setRecords] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    getHealthRecords(1).then(setRecords).catch((requestError) => setError(requestError.message));
  }, []);

  return (
    <section className="page">
      <p className="eyebrow">HEALTH TRENDS</p>
      <h2>Saved synthetic check-ins</h2>
      <p className="muted">Each line shows records stored in the local SQLite database.</p>
      {error ? <p className="message error">{error}</p> : <HealthTrends records={records} />}
      <p className="disclaimer">Charts describe synthetic demo data only. They do not provide medical advice.</p>
    </section>
  );
}
