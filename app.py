from fastapi import FastAPI

app = FastAPI(title="Inference API")


@app.get("/")
async def root():
    return {"message": "inference model test"}