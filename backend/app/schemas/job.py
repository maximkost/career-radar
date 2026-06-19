from pydantic import BaseModel, ConfigDict


class Job(BaseModel):
    id: int
    title: str
    company: str
    location: str
    source: str
    description: str
    posted_date: str | None = None

    model_config = ConfigDict(from_attributes=True)

class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    source: str
    description: str
    posted_date: str | None = None
