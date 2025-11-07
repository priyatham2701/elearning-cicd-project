from fastapi import FastAPI

app = FastAPI(title="svc-students", description="Students service manages student profiles and progress.")

@app.get("/")
def root():
    return {"service": "svc-students", "message": "elearning microservice"}

@app.get("/health")
def health():
    return {"service": "svc-students", "status": "ok"}
