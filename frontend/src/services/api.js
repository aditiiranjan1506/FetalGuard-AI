const API_BASE_URL = "http://127.0.0.1:8000";

async function request(path, options) {
  const response = await fetch(`${API_BASE_URL}${path}`, options);
  if (!response.ok) throw new Error("The server could not complete that request.");
  return response.json();
}

export async function submitHealthRecord(patientId, healthRecord) {
  return request(`/api/health-records/${patientId}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(healthRecord),
  });
}

export function getDashboard(patientId) {
  return request(`/api/dashboard/${patientId}`);
}

export function getHealthRecords(patientId) {
  return request(`/api/health-records/${patientId}`);
}
