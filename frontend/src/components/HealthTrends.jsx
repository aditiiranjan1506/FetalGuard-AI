import {
  CartesianGrid,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

function SmallLineChart({ data, dataKey, color, title, unit }) {
  return (
    <article className="chart-card">
      <h3>{title}</h3>
      <ResponsiveContainer width="100%" height={230}>
        <LineChart data={data} margin={{ top: 8, right: 16, left: -14, bottom: 4 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="week" label={{ value: "Pregnancy week", position: "insideBottom", offset: -2 }} />
          <YAxis width={44} />
          <Tooltip formatter={(value) => [`${value} ${unit}`, title]} />
          <Line type="monotone" dataKey={dataKey} stroke={color} strokeWidth={3} dot />
        </LineChart>
      </ResponsiveContainer>
    </article>
  );
}

export default function HealthTrends({ records }) {
  const chartData = records.map((record) => ({
    week: `W${record.pregnancy_week}`,
    systolic: record.systolic_bp,
    diastolic: record.diastolic_bp,
    heartRate: record.heart_rate,
    weight: record.weight,
  }));

  if (!chartData.length) return <p className="muted">No saved records yet.</p>;

  return (
    <div className="chart-grid">
      <SmallLineChart data={chartData} dataKey="systolic" color="#c05b42" title="Systolic blood pressure" unit="mmHg" />
      <SmallLineChart data={chartData} dataKey="heartRate" color="#126a9d" title="Heart rate" unit="bpm" />
      <SmallLineChart data={chartData} dataKey="weight" color="#16835f" title="Weight" unit="kg" />
    </div>
  );
}
