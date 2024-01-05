from fastapi import FastAPI, Body

from pydantic import BaseModel

import copy

app = FastAPI()

# Database
posts_database = dict()
posts_database["counter_id"] = 0

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
        posts_database[str(posts_database["counter_id"])] = post
        posts_database["counter_id"] += 1
        return {"message": f"post {post.title} appended sucessfully"}
    except Exception as e:
        return {"message": f"Error: {e}"}

@app.get("/posts/read-all-post")
def read_all_post():
    try:
        db_copy = copy.deepcopy(posts_database)
        del db_copy["counter_id"]
        return db_copy
    except Exception as e:
        return {"message": f"Error: {e}"}

@app.get("/posts/read-post/{id}")
def read_post(id):
    try:
        return posts_database[id]
    except Exception as e:
        return {"message": f"Error: {e}"}
    
@app.delete("/posts/delete-post/{id}")
def delete_post(id):
    try:
        value = posts_database.pop(id, None)
        return {"message": f"post {id} with title {value.title} was deleted"}
    except Exception as e:
        return {"message": f"Error: {e}"}