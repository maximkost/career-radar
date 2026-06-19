def test_get_jobs_returns_empty_list(client):
    response = client.get("/jobs")

    assert response.status_code == 200
    assert response.json() == []


def test_create_job(client, job_payload):
    response = client.post("/jobs/", json=job_payload)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] is not None
    assert data["title"] == job_payload["title"]
    assert data["company"] == job_payload["company"]
    assert data["location"] == job_payload["location"]
    assert data["source"] == job_payload["source"]
    assert data["description"] == job_payload["description"]
    assert data["posted_date"] == job_payload["posted_date"]


def test_get_jobs_returns_created_jobs(client, sample_job):
    response = client.get("/jobs")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == sample_job.id
    assert data[0]["title"] == sample_job.title


def test_get_job_by_id(client, sample_job):
    response = client.get(f"/jobs/{sample_job.id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == sample_job.id
    assert data["title"] == sample_job.title


def test_get_job_by_id_invalid_id(client):
    response = client.get("/jobs/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Job not found"}


def test_delete_job(client, sample_job):
    response = client.delete(f"/jobs/{sample_job.id}")

    assert response.status_code == 200
    assert response.json() == {"detail": f"Job {sample_job.id} deleted"}

    get_response = client.get(f"/jobs/{sample_job.id}")
    assert get_response.status_code == 404


def test_delete_job_invalid_id(client):
    response = client.delete("/jobs/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Job not found"}
