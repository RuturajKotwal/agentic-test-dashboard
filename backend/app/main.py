from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import test_runs

app = FastAPI(
    title="Agentic Test Dashboard API",
    version="1.0.0"
)

# Configure CORS so Vue frontend (running on port 5173) can talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(test_runs.router, prefix="/api/v1/test-runs", tags=["Test Runs"])

@app.get("/")
async def root():
    return {"message": "Agentic Test Dashboard API is running"}