from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from datetime import datetime

TestStatus = Literal['passed', 'failed', 'running', 'pending']

# 1. The input schema (What the client sends in a POST request)
class TestRunCreate(BaseModel):
    name: str
    status: TestStatus = 'pending'
    duration_ms: Optional[int] = None

# 2. The output schema (What we return to the client)
class TestRun(BaseModel):
    id: str
    name: str
    status: TestStatus
    duration_ms: Optional[int] = None
    started_at: datetime

    # This tells Pydantic: "It's okay to read data directly from a SQLAlchemy ORM object"
    model_config = ConfigDict(from_attributes=True)