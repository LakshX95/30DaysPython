from fastapi import FastAPI
from fastapi import Request

app = FastAPI()
@app.get("/")
async def read_root():
    return {"message": "Welcome to the API Exercise!"}

@app.get("/hello")
async def say_hello():
    return {"geeting": "Hello, World!"}

@app.post("/echo")
async def echo_message(request: Request):
    data = await request.json()
    return {"received": data}

@app.get("user/{username}")
def greet_user(username: str):
    return {"message": f"Hello, {username}!"}