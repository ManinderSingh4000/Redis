from fastapi import FastAPI , APIRouter , HTTPException

app = FastAPI(
    title="Dashboard Arena", 
    version="1.4.8"

)

datastore ={
    "_id" : [123,125,126,127],
    "Name" : ["Maninder" ,"Diksha" , "Mamta" , "Shavnam"],
    "City" : ["SBNR" , "Mansa" ,"Firozpur", "Kangra"]
}

@app.get("/")
async def index():
    return {"Message : This is The Dashboard Index Page"}

@app.get("/v1/info/")
async def get_info():
    return {
        "_id": datastore["_id"],
        "Name" : datastore["Name"]
    }

@app.get("/v1/info/{id}")
async def get_info_specific(_id : int):
    if _id not in datastore["_id"]:
        raise HTTPException(status_code=404 , detail="Data Does not Exist")
    
    index = datastore["_id"].index(_id)

    return {
        "_id": datastore["_id"][index],
        "Name" : datastore["Name"][index]
    }


@app.get("/v2/info")
async def get_info():
    return {
        "_id": datastore["_id"],
        "Name" : datastore["Name"],
        "City" : datastore["City"]
    }

@app.get("/v2/info/{id}")
async def get_info_specific(_id : int):

    if _id not in datastore["_id"]:
        raise HTTPException(status_code=404 , detail=" ID does not Exist ")
    
    index = datastore["_id"].index(_id)

    return {
        "_id" : datastore["_id"][index],
        "Name" : datastore["Name"][index],
        "City" : datastore["City"][index]
    }