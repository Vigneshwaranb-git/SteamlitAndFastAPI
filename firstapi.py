import fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/bookes/{book_name}")
async def read_item(book_name: str, q: str = None):
    return {"book_name": book_name, "q": q}