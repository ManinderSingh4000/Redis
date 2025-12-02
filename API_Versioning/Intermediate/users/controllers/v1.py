from fastapi import FastAPI, APIRouter, HTTPException   
from data.data import datastore

v1 = APIRouter(prefix="/v1/info" , tags=["V1 API's"])

@v1.get("/students")
async def get_users():
    return {
        "_id" : datastore['_id'],
        "Name" : datastore['Name']
    }

@v1.get("/students/{_id}")
async def get_specific_user(_id : int):
    if _id not in datastore["_id"]:
        raise HTTPException(status_code=404 , detail=" Student ID Does not Exist")

    index = datastore["_id"].index(_id)

    return {
        "_id": datastore["_id"][index],
        "Name" : datastore['Name'][index]
    
    }