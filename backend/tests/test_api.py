from fastapi.testclient import TestClient
from app.main import app

# Instantiate the test client with our FastAPI app
client = TestClient(app)

def test_root_endpoint():
    """Test that the API health check is responding."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Agentic Test Dashboard API is running"}

def test_get_test_runs():
    """Test the test-runs endpoint to ensure it returns a valid list of runs."""
    response = client.get("/api/v1/test-runs/")
    
    # 1. Assert the request was successful
    assert response.status_code == 200
    
    # 2. Extract the JSON payload
    data = response.json()
    
    # 3. Assert we are getting a list
    assert isinstance(data, list)
    assert len(data) == 3 # We expect our 3 mock items
    
    # 4. Assert the structure of the first item strictly matches our Pydantic schema requirements
    first_run = data[0]
    assert "id" in first_run
    assert "name" in first_run
    assert "status" in first_run
    assert "started_at" in first_run
    
    # 5. Assert specific data types or values
    assert first_run["status"] in ["passed", "failed", "running", "pending"]