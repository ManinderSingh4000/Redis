from routes.v2_routes import router as v2_router
from fastapi import  HTTPException
from routes.v2_routes import router 
from data.data import datastore


@router.get("/users")
async def get_all_users():
    return datastore

@router.get("/users/{_id}" )
async def get_user_by_id(_id: int ):
    if _id not in datastore["_id"]:
        raise HTTPException(status_code=404, detail="User ID Does not Exist")
    index = datastore["_id"].index(_id)

    return {
        "_id": datastore["_id"][index],
        "Name": datastore["name"][index],
        "City": datastore["city"][index]
    }
    
