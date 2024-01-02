from fastapi import FastAPI, Body

from pydantic import BaseModel

app = FastAPI()

# Database
posts_database = []

# Models

class Post(BaseModel):
    title: str
    content: str

@app.get("/")
def home():
    return {"message": "hello world"}


@app.post("/posts/create_post")
def create_post(post: Post=Body(...)):
    try:
        posts_database.append(post)
        return {"message": f"post {post.title} appended sucessfully"}
    except Exception as e:
        return {"message": f"Error: {e}"}
