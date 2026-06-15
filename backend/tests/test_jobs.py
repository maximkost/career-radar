from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_jobs():
    response = client.get("/jobs")
    assert response.status_code == 200

def test_get_job_by_id():
    response = client.get("/jobs/1")
    assert response.status_code == 200

def test_get_job_by_id_invalid_id():
    response = client.get("/jobs/999")
    assert response.status_code == 404
