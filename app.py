import httpx
from fastapi import FastAPI
from redis import Redis
import json

app = FastAPI(
    title="Dashboard",
    version="1.4.4"   
    )

@app.on_event("startup")
async def startup():
    app.state.redis = Redis(
        host = "localhost",
        port = 6379
    )
    app.state.http_client = httpx.AsyncClient()



@app.on_event('shutdown')
async def close():
    app.state.redis.close()


@app.get("/")
def index():
    return {"message : FastAPI + Redis is working"}

@app.get("/Entries")
async def read_data():
    headers = {
        "Authorization": f"Bearer {"7a8219b992074b6493eb58636e321482"}",   # or: "X-API-Key": API_KEY
        "Content-Type": "application/json"
    }

    result = await app.state.http_client.get("https://api.housecallpro.com/customers" , headers = headers)

    return result.json()