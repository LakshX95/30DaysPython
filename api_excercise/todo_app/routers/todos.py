
from fastapi import APIRouter

router = APIRouter()
todos = []


@router.get("/todos")
async def get_todos():
    return {"todos": todos}


@router.post("/todos")
async def add_todo(item: str):
    todos.append(item)
    return {"message": "Todo item added", "todos": todos}


@router.put("/todos/{item_id}")
async def update_todo(item_id: int, item: str):
    if 0 <= item_id < len(todos):
        todos[item_id] = item
        return {"message": "Todo item updated", "todos": todos}
    return {"error": "Item not found"}, 404


@router.delete("/todos/{item_id}")
async def delete_todo(item_id: int):
    if 0 <= item_id < len(todos):
        removed_item = todos.pop(item_id)
        return {"message": "Todo item deleted", "removed": removed_item, "todos": todos}
    return {"error": "Item not found"}, 404
