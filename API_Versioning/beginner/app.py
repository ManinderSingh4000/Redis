from fastapi import FastAPI , APIRouter , HTTPException

app = FastAPI(
    version="1.3.7",
    title= "FastAPI Dashboard",
    summary="Ithe Ki Krn Deya aa Penchoda",
    
)
v1Router = APIRouter(prefix="/v1/apis" , tags=["V1 API's"])
v2Router = APIRouter(prefix="/v2/apis" , tags=["V2 API's"])

datastore ={
    "_id" : [123,125,126,127],
    "Name" : ["Maninder" ,"Diksha" , "Mamta" , "Shavnam"],
    "City" : ["SBNR" , "Mansa" ,"Firozpur", "Kangra"]
}

@app.get("/")
def index():
    return {"Message": "Welcome in The Dashboard"}


@v1Router.get("/users")
async def get_users():
    return {
        "_id" : datastore['_id'],
        "Name" : datastore['Name']
    }

@v1Router.get("/users/{_id}")
async def get_specific_user(_id : int):
    if _id not in datastore["_id"]:
        raise HTTPException(status_code=404 , detail=" Student ID Does not Exist")

    index = datastore["_id"].index(_id)

    return {
        "_id": datastore["_id"][index],
        "Name" : datastore['Name'][index]
    
    } 


@v2Router.get("/users/{_id}")
async def get_specific_user(_id : int):
    if _id not in datastore["_id"]:
        raise HTTPException(status_code=404 , detail="Student ID Does not Exist")
    index = datastore["_id"].index(_id)
    return {
        "_id" : datastore["_id"][index],
        "Name": datastore["Name"][index],
        "City": datastore['City'][index]
    }

@v2Router.get("/users")
async def get_users():
    return datastore

app.include_router(v1Router)
app.include_router(v2Router)
