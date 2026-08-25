"""Phase 2: the small SQLite connection used by the prototype."""

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_FILE = Path(__file__).parent.parent / "fetalguard.db"
engine = create_engine(f"sqlite:///{DATABASE_FILE}", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    pass


def get_db():
    """Give one database session to a request, then close it afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
