from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import uuid4

app = FastAPI(title="Balance Backend MVP", version="0.1.0")

class RegisterRequest(BaseModel):
    app_version: str = Field(..., example="0.1.0")
    device: dict = Field(
        ...,
        example={
            "platform": "android",
            "model": "Motorola Moto G73",
            "os_version": "14"
        }
    )

class RegisterResponse(BaseModel):
    pid: str
    created_at: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/v1/register", response_model=RegisterResponse, status_code=201)
def register(req: RegisterRequest):
    pid = str(uuid4())
    created_at = datetime.now(timezone.utc).isoformat()
    return RegisterResponse(pid=pid, created_at=created_at)
