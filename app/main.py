from fastapi import FastAPI

from app.api.tasks import router as tasks_router
from app.core.database import Base, engine
from app.core.exceptions import add_exception_handlers

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="API para gestionar tareas",
    version="1.0.0"
)

add_exception_handlers(app)

app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])


@app.get("/")
def root():
    return {"message": "Task Manager API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}
