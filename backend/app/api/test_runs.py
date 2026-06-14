from fastapi import APIRouter
from typing import List
from datetime import datetime, timezone
from app.models.schemas import TestRun

router = APIRouter()

@router.get("/", response_model=List[TestRun])
async def get_test_runs():
    """
    Fetch all test runs. 
    Currently returns mock data. Will integrate with MySQL in Milestone 4.
    """
    mock_data = [
        {
            "id": "tr_1",
            "name": "Authentication Flow",
            "status": "passed",
            "duration_ms": 1200,
            "started_at": datetime.now(timezone.utc)
        },
        {
            "id": "tr_2",
            "name": "Payment Gateway Integration",
            "status": "failed",
            "duration_ms": 4500,
            "started_at": datetime.now(timezone.utc)
        },
        {
            "id": "tr_3",
            "name": "User Profile Sync",
            "status": "running",
            "duration_ms": None,
            "started_at": datetime.now(timezone.utc)
        }
    ]
    return mock_data