from pydantic import BaseModel

class Job(BaseModel):
    id: int
    title: str
    company: str
    location: str
    source: str
    description: str
    posted_date: str | None = None

class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    source: str
    description: str
    posted_date: str | None = None
