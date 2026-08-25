import { useState } from "react";
import Dashboard from "./pages/Dashboard";
import DailyCheckIn from "./pages/DailyCheckIn";
import Navigation from "./components/Navigation";
import HealthTrendsPage from "./pages/HealthTrendsPage";

export default function App() {
  // This small app uses local state instead of adding a routing library.
  const [currentPage, setCurrentPage] = useState("dashboard");

  return (
    <main className="app-shell">
      <Navigation currentPage={currentPage} onNavigate={setCurrentPage} />
      {currentPage === "dashboard" && <Dashboard />}
      {currentPage === "check-in" && <DailyCheckIn />}
      {currentPage === "trends" && <HealthTrendsPage />}
    </main>
  );
}
