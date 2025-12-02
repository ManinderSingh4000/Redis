import json
import httpx
from fastapi import FastAPI
from redis import Redis
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

URL = os.getenv("URL")
API_KEY = os.getenv("API_KEY")

@app.on_event("startup")
async def startup():
    app.state.redis = Redis(
        host="localhost",
        port= 6379,
        decode_responses=True
    )
    app.state.http_client = httpx.AsyncClient()

@app.on_event("shutdown")
async def closeup():
    app.state.redis.close()

@app.get("/")
def index_page():
    return "Message : Welcome in The Dashboard Page"


@app.get("/entries")
async def read_customers():

    cache = app.state.redis.get("entries")

    if cache:
        return json.loads(cache)
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",   # or: "X-API-Key": API_KEY
        "Content-Type": "application/json"
    }
    

    response = await app.state.http_client(headers , URL)

    result = response.json()

    app.state.redis.set("entries" , json.dumps(result))

    return result    