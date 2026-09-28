from fastapi import FastAPI
from .database import Base, engine
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tender Document Verification System",
    description="AI-powered tender document verification system",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Tender Verification System Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }