from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    author: str
    lines: int


class NewTask(BaseModel):
    title: str
    author: str
    lines: int


library = {
    0: Task(id=0, title="Python1", author="fahd", lines = 15),
    1: Task(id=1, title="fast api", author="fahd ", lines=50),
}
next_id = len(library)


@app.get("/")
def home():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/health")
def health():
    return { "status": "ok" }

@app.get("/tasks")
def all_tasks():
    return list(library.values())

@app.get("/tasks/{id}")
def get_task(id : int):
    if id not in library:
        return HTTPException(status_code=404, detail=f"Task with {id} not found")
    return library[id]

@app.put("/tasks")
def update_task(task : Task):
    library[task.id] = task
    return task
    
@app.delete("/tasks/{id}")
def delete_task(id : int):
    library.pop(id)
    return f"Task {id} succssefully deleted"

@app.post("/task")
def create_task(task : NewTask):
    global next_id
    new_task = Task(id= next_id, title=task.title, author=task.author, lines=task.lines)
    library[next_id] = new_task
    return "New task is added successfully"
    