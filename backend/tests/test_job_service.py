from app.services.job_service import (
    create_job,
    delete_job,
    get_all_jobs,
    get_job_by_id,
)
from app.schemas.job import JobCreate


def test_get_all_jobs_returns_empty_list(db_session):
    assert get_all_jobs(db_session) == []


def test_create_job(db_session, job_payload):
    job = create_job(db_session, JobCreate(**job_payload))

    assert job.id is not None
    assert job.title == job_payload["title"]
    assert job.company == job_payload["company"]


def test_get_all_jobs_returns_created_jobs(db_session, sample_job):
    jobs = get_all_jobs(db_session)

    assert len(jobs) == 1
    assert jobs[0].id == sample_job.id


def test_get_job_by_id_returns_job(db_session, sample_job):
    job = get_job_by_id(db_session, sample_job.id)

    assert job is not None
    assert job.id == sample_job.id
    assert job.title == sample_job.title


def test_get_job_by_id_returns_none_for_missing_job(db_session):
    assert get_job_by_id(db_session, 999) is None


def test_delete_job_removes_existing_job(db_session, sample_job):
    result = delete_job(db_session, sample_job.id)

    assert result is True
    assert get_job_by_id(db_session, sample_job.id) is None


def test_delete_job_returns_false_for_missing_job(db_session):
    assert delete_job(db_session, 999) is False
