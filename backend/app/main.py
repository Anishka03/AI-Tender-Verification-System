from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    debug=settings.DEBUG,
)


# --------------------------------------------------
# CORS CONFIGURATION
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# ROOT ENDPOINT
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "AI-Powered Tender Document Verification API",
        "status": "running",
        "environment": settings.APP_ENV,
    }


# --------------------------------------------------
# APPLICATION HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "FastAPI",
    }


# --------------------------------------------------
# DATABASE HEALTH CHECK
# --------------------------------------------------

@app.get("/health/database")
def database_health_check(
    db: Session = Depends(get_db),
):
    try:
        result = db.execute(text("SELECT 1"))
        value = result.scalar()

        return {
            "status": "healthy",
            "database": "MySQL",
            "connection": True,
            "test_result": value,
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "MySQL",
            "connection": False,
            "error": str(e),
        }