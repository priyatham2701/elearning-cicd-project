from fastapi import FastAPI

app = FastAPI(title="svc-courses", description="Courses service manages the course catalog.")

@app.get("/")
def root():
    return {"service": "svc-courses", "message": "elearning microservice"}

@app.get("/health")
def health():
    return {"service": "svc-courses", "status": "ok"}
