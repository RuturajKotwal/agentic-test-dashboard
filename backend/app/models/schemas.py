from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Python uses Enums or Literal types. We'll use Literal for simplicity here to match TS.
from typing import Literal

TestStatus = Literal['passed', 'failed', 'running', 'pending']

class TestRun(BaseModel):
    id: str
    name: str
    status: TestStatus
    duration_ms: Optional[int] = None
    started_at: datetime