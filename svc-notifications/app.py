from fastapi import FastAPI

app = FastAPI(title="svc-notifications", description="Notifications service sends notifications to learners and instructors.")

@app.get("/")
def root():
    return {"service": "svc-notifications", "message": "elearning microservice"}

@app.get("/health")
def health():
    return {"service": "svc-notifications", "status": "ok"}
