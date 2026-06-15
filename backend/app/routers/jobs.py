from fastapi import APIRouter, HTTPException
import app.services.job_service as service
from app.schemas.job import Job, JobCreate

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/", response_model=list[Job])
def get_jobs():
    return service.get_all_jobs()


@router.get("/{job_id}", response_model=Job)
def get_job_by_id(job_id: int):
    job = service.get_job_by_id(job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.post("/", response_model=Job)
def create_job(job: JobCreate):
    return service.create_job(job)

@router.delete("/{job_id}")
def delete_job(job_id: int):
    if not service.delete_job(job_id):
        raise HTTPException(status_code=404, detail="Job not found")
