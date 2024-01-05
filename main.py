from fastapi import FastAPI, Body

from pydantic import BaseModel

from subjects.posts import posts

app = FastAPI()

app.include_router(posts.router)

@app.get("/")
def root():
    return {"message": "Hello World"}         