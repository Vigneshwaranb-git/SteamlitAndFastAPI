import fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Welcome to FastAPI!"}

@app.get("/books/{book_name}")
def read_item(book_name: str, q: str = "FastAPI is awesome!"):
    return {"book_name": book_name, "q": q}