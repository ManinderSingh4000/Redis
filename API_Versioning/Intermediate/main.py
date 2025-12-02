from fastapi import FastAPI , APIRouter , HTTPException
from users.controllers.v1 import v1
from users.controllers.v2 import v2


app= FastAPI(
    title="Dashboard Arena",
    version="1.4.8"
)

app.include_router(v1)
app.include_router(v2)


@app.get("/")
async def index():  
    return {"Message" : "This is The Dashboard Index Page"}