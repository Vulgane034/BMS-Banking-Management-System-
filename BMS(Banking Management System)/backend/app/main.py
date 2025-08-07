from fastapi import FastAPI
from app.api import auth, data, recommendation, upload

app = FastAPI(title="BMS Backend API")

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(data.router, prefix="/api/data", tags=["data"])
app.include_router(recommendation.router, prefix="/api/recommendation", tags=["recommendation"])
app.include_router(upload.router, prefix="/api/upload", tags=["upload"])