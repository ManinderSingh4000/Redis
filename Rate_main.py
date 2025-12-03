from fastapi import FastAPI, HTTPException, Request
from Rate_Limiter import rate_limiter
from Redis_client import redis_client

app = FastAPI()

datastore = {
    "_id": [121, 122, 123, 124],
    "name": ["Maninder", "Harsh", "Anmol", "AgamPreet"],
    "city": ["Chandigarh", "Patiala", "Ludhiana", "Amritsar"],
}

@app.get("/info")
async def get_info(request: Request):

    client_ip = request.client.host

    key = f"rate:{client_ip}"

    allowed = rate_limiter(key, limit=4, window_seconds=10)

    if not allowed:
        raise HTTPException(
            status_code=429,
            detail="Too Many Requests"
        )

    return datastore


@app.get("/reset-rate")
def reset():
    redis_client.delete("rate:127.0.0.1")
    return {"status": "reset-done"}
