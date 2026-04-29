from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello dear", "custom_key": "custom_value"}
