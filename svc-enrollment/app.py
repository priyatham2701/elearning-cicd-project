from fastapi import FastAPI

app = FastAPI(title="svc-enrollment", description="Enrollment service manages course registrations and seats.")

@app.get("/")
def root():
    return {"service": "svc-enrollment", "message": "elearning microservice"}

@app.get("/health")
def health():
    return {"service": "svc-enrollment", "status": "ok"}
