import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from datetime import datetime, timezone

from app.models.schemas import TestRun, TestRunCreate
from app.models.db_models import DBTestRun
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=List[TestRun])
async def get_test_runs(db: AsyncSession = Depends(get_db)):
    """Fetch all test runs from MySQL, ordered by newest first."""
    # Build the query
    stmt = select(DBTestRun).order_by(DBTestRun.started_at.desc())
    
    # Execute asynchronously
    result = await db.execute(stmt)
    
    # Extract the scalar values (the actual DBTestRun objects)
    runs = result.scalars().all()
    
    return runs

@router.post("/", response_model=TestRun, status_code=201)
async def create_test_run(run_in: TestRunCreate, db: AsyncSession = Depends(get_db)):
    """Create a new test run in the database."""
    # Generate a unique ID for the test run (e.g., tr_a1b2c3d4)
    new_id = f"tr_{uuid.uuid4().hex[:8]}"
    
    # Map the Pydantic input schema to the SQLAlchemy database model
    new_run = DBTestRun(
        id=new_id,
        name=run_in.name,
        status=run_in.status,
        duration_ms=run_in.duration_ms,
        started_at=datetime.now(timezone.utc)
    )
    
    # Add to the session and commit to the database
    db.add(new_run)
    await db.commit()
    
    # Refresh retrieves the exact state from the database (just to be safe)
    await db.refresh(new_run)
    
    return new_run