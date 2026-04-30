from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "custom_key": "custom_value"}


@app.get("/posts")
async def get_posts():
    return {"data": "here will be your posts!"}
