from fastapi.testclient import TestClient
from app.main import app

# Create a test client that mimics a frontend making requests
client = TestClient(app)

def test_root_endpoint():
    """Ensure the API root is accessible."""
    response = client.get("/")
    assert response.status_code == 200

def test_get_test_runs_empty():
    """Ensure a fresh database returns an empty list."""
    response = client.get("/api/v1/test-runs/")
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # The database starts empty, so we expect a length of 0
    assert len(data) == 0 

def test_create_test_run():
    """Ensure we can successfully create a new test run in the database."""
    payload = {
        "name": "CI Automated Test",
        "status": "passed",
        "duration_ms": 120
    }
    
    response = client.post("/api/v1/test-runs/", json=payload)
    
    # 201 is the HTTP status code for "Created"
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == "CI Automated Test"
    assert data["status"] == "passed"
    # Ensure the database generated an ID and timestamp for us
    assert "id" in data
    assert "started_at" in data