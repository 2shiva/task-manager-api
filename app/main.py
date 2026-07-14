from fastapi import FastAPI

from app.database import Base, engine
from app.models import Task, User
from app.routes.tasks import router as task_router
from app.auth import router as auth_router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="Backend Developer Assignment",
    version="1.0.0"
)

# Include Routers
app.include_router(task_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Task Manager API is running!"}