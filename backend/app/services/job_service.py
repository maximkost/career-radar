from sqlalchemy.orm import Session

from app.models.jobs import Job
from app.schemas.job import JobCreate


def get_all_jobs(db: Session):
    return db.query(Job).all()


def get_job_by_id(db: Session,job_id: int):
    return db.query(Job).filter(Job.id == job_id).first()


def create_job(db: Session,job: JobCreate):
    db_job = Job(**job.model_dump())

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job


def delete_job(db: Session, job_id: int):
    job = get_job_by_id(db, job_id)

    if job is None:
        return False

    db.delete(job)
    db.commit()
    return True
