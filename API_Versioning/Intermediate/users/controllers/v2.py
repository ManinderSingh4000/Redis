from fastapi import FastAPI , APIRouter , HTTPException
from data.data import datastore

v2 = APIRouter(prefix="/v2/info" , tags=["V2 API's"])

@v2.get("/studnents")
async def get_users():

    return {
        "_id" : datastore['_id'],
        "Name" : datastore['Name'],
        "City" : datastore['City']
    }

@v2.get("/students/{_id}")
async def get_specific_user(_id : int):
    if _id not in datastore["_id"]:
        raise HTTPException(status_code=404 , detail="Student ID Does not Exist"
                        )
    index = datastore["_id"].index(_id)

    return {
        "_id" : datastore["_id"][index],
        "Name": datastore["Name"][index],
        "City": datastore['City'][index]
    }