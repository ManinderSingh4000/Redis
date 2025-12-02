from fastapi import FastAPI
from controllers.v1Controller import router as v1_router
from controllers.v2Controller import router as v2_router

app = FastAPI()

app.include_router(v1_router)
app.include_router(v2_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the API Versioning Example!"}