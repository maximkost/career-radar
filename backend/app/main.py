from fastapi import FastAPI

from app.routers import jobs

app = FastAPI()

@app.get("/")
def root():
    return {"Status": "ok"}

app.include_router(jobs.router)
