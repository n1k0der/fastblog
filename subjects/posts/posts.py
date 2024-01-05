from fastapi import APIRouter, Body

from pydantic import BaseModel

import copy

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

# Database
posts_database = dict()
posts_database["counter_id"] = 0

# Models

class Post(BaseModel):
    title: str
    content: str


@router.post("/create_post")
def create_post(post: Post=Body(...)):
    try:
        posts_database[str(posts_database["counter_id"])] = post
        posts_database["counter_id"] += 1
        return {"message": f"post {post.title} appended sucessfully"}
    except Exception as e:
        return {"message": f"Error: {e}"}

@router.get("/read-all-post")
def read_all_post():
    try:
        db_copy = copy.deepcopy(posts_database)
        del db_copy["counter_id"]
        return db_copy
    except Exception as e:
        return {"message": f"Error: {e}"}

@router.get("/read-post/{id}")
def read_post(id):
    try:
        return posts_database[id]
    except Exception as e:
        return {"message": f"Error: {e}"}
    
@router.delete("/delete-post/{id}")
def delete_post(id):
    try:
        value = posts_database.pop(id, None)
        return {"message": f"post {id} with title {value.title} was deleted"}
    except Exception as e:
        return {"message": f"Error: {e}"}