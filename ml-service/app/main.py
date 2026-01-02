from fastapi import FastAPI
from app.api import resume,health

app = FastAPI(title = "CareerCraft ML Service")

app.include_router(health.router, prefix="/health", tags=["System"])
app.include_router(resume.router, prefix="/resume", tags=["Extraction"])

@app.get("/")
async def root():
    return {"message": "ML Service is running"}