from Redis_client import redis_client

def rate_limiter(
        key :str,
        limit : int ,
        window_seconds : int
    ):
    
    current = redis_client.incr(key)

    if current==1:
        redis_client.expire(key , window_seconds)
    
    if current > limit:
        return False
    return True