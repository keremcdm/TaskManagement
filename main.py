from fastapi import FastAPI
from auth import router as auth_router
from tasks import router as tasks_router

app = FastAPI(title="TaskManager API")

@app.get("/")
def root():
    return {"message": "TaskManager API is running!"}

app.include_router(auth_router)
app.include_router(tasks_router)
