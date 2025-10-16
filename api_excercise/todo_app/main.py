todos = []
from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the TODO App Exercise!"}

# Import and include the todos router
from .routers.todos import router as todos_router
app.include_router(todos_router)
