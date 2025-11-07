from fastapi import FastAPI

app = FastAPI(title="svc-instructors", description="Instructors service manages instructors and their courses.")

@app.get("/")
def root():
    return {"service": "svc-instructors", "message": "elearning microservice"}

@app.get("/health")
def health():
    return {"service": "svc-instructors", "status": "ok"}
