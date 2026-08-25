export default function Navigation({ currentPage, onNavigate }) {
  return (
    <nav className="navigation" aria-label="Main navigation">
      <div>
        <p className="eyebrow">SYNTHETIC-DEMO PROTOTYPE</p>
        <h1>FetalGuard AI</h1>
      </div>
      <div className="nav-links">
        <button
          className={currentPage === "dashboard" ? "active" : ""}
          onClick={() => onNavigate("dashboard")}
        >
          Dashboard
        </button>
        <button
          className={currentPage === "check-in" ? "active" : ""}
          onClick={() => onNavigate("check-in")}
        >
          Daily Check-In
        </button>
        <button
          className={currentPage === "trends" ? "active" : ""}
          onClick={() => onNavigate("trends")}
        >
          Health Trends
        </button>
      </div>
    </nav>
  );
}
