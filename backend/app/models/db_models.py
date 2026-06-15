from sqlalchemy import Column, String, Integer, DateTime
from app.db.session import Base
from datetime import datetime, timezone

class DBTestRun(Base):
    __tablename__ = "test_runs"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False)
    duration_ms = Column(Integer, nullable=True)
    started_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)