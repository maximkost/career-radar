from fastapi import APIRouter, HTTPException
import app.services.job_service as service
from app.schemas.job import Job, JobCreate

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/", response_model=list[Job])
def get_jobs(db: Session = Depends(get_db)):
    return service.get_all_jobs(db)


@router.get("/{job_id}", response_model=Job)
def get_job_by_id(job_id: int, db: Session = Depends(get_db)):
    job = service.get_job_by_id(db, job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.post("/", response_model=Job)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return service.create_job(db, job)

@router.delete("/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    if not service.delete_job(db, job_id):
        raise HTTPException(status_code=404, detail="Job not found")

    return {"detail": f"Job {job_id} deleted"}
