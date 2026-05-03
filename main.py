from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    # content: Optional[str] = None # this or
    content: str | None = None
    published: bool = (
        True  # if a default value is provided, fastapi makes that property Optional
    )
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World", "custom_key": "custom_value"}


@app.get("/posts")
async def get_posts():
    return {"data": "here will be your posts!"}


@app.post("/createposts")
async def create_posts(payload: Post):
    print(payload.model_dump())
    return {
        "new_post": payload.title,
        "content": payload.content,
        "published": payload.published,
        "ratings": payload.rating,
    }
