from fastapi import FastAPI

from app.routers import jobs

app = FastAPI()

@app.get("/")
def read_root():
    return {"name": "Career Radar API",
            "version": "0.1.0",
            "description": "Backend API for CareerRadar",}

@app.get("/health")
def health():
    return {"Status": "ok"}

app.include_router(jobs.router)
