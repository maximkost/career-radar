from app.schemas.job import JobCreate

mock_data = [
    {
        "id": 1,
        "title": "Junior Python Developer",
        "company": "TechStart",
        "location": "Tallinn, Estonia",
        "source": "mock",
        "description": "Build REST APIs with Python, FastAPI, SQL, and Git.",
        "posted_date": "2026-06-10",
    },
    {
        "id": 2,
        "title": "Software Engineer Intern",
        "company": "DataLab",
        "location": "Remote",
        "source": "mock",
        "description": "Internship for students with Python, PostgreSQL, and Docker basics.",
        "posted_date": "2026-06-12",
    },
]


def get_all_jobs():
    return mock_data


def get_job_by_id(job_id: int):
    for job in mock_data:
        if job["id"] == job_id:
            return job
    return None


def create_job(job: JobCreate):
    new_job = {
        "id": len(mock_data) + 1,
        "title": job.title,
        "company": job.company,
        "location": job.location,
        "source": job.source,
        "description": job.description,
        "posted_date": job.posted_date,
    }

    mock_data.append(new_job)
    return new_job


def delete_job(job_id):
    job = get_job_by_id(job_id)
    if job is not None:
        mock_data.remove(job)
        return True
    return False
