from fastapi import FastAPI

# from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "custom_key": "custom_value"}


@app.get("/posts")
async def get_posts():
    return {"data": "here will be your posts!"}


class Post(BaseModel):
    title: str
    # content: Optional[str] = None # this or
    content: str | None = None


@app.post("/createposts")
async def create_posts(payload: Post):
    print(payload)
    return {"new_post": payload.title, "content": payload.content}
