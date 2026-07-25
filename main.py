from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import database

app = FastAPI()


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str
    done: bool


@app.get("/")
def home():
    return {"message": "API is running"}


@app.get("/tasks")
def get_tasks():
    return database.get_all_tasks()


@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    task = database.get_task_by_id(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@app.post("/tasks", status_code=201)
def add_task(task: TaskCreate):

    if task.title.strip() == "":
        raise HTTPException(status_code=400, detail="Title required")

    return database.create_task(task.title)


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):

    updated_task = database.update_task(
        task_id,
        task.title,
        task.done
    )

    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return updated_task

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):

    deleted = database.delete_task(task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")