from fastapi import FastAPI

app = FastAPI()

@app.net("/helloworld")
async def read_root():
    return {"Message":"Hello world congrats"}