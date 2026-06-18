from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Temporary in-memory database
todos = []

# Pydantic Schema
class Todo(BaseModel):
    id: int
    title: str
    completed: bool

# 127.0.0.1:8000/todos
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "message": "Todo added",
        "data": todo
    }


# Fetch all Todos
@app.get("/todos")
def get_todos():
    return todos

# Fetch a single Todo by ID
@app.get("/todos/{todo_id}")
def get_single_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            # Replace the old todo with the new data
            todos[index] = updated_todo
            return {
                "message": "Data updated",
                "data": updated_todo
            }
    return {"error": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            # Remove the item from the list
            todos.pop(index)
            return {"message": "Data deleted"}
    return {"error": "Todo not found"}