from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    completed: bool = False

todos_pydantic: List[Todo] = []

@app.post("/todos/pydantic")
def add_todo_pydantic(todo: Todo):
    todos_pydantic.append(todo)
    return {"message": "Todo added", "todos": todos_pydantic}