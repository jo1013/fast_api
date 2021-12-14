from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

import recommendation as rd

app = FastAPI()


class Item(BaseModel):
    userid : int
    recomand : List[str] = []
    
    
@app.get("/")
async def read_root():
    return {"Hello": "World"}
    

@app.get("/items/{user_id}")
async def read_id(user_id: int):
    t = rd.reco(user_id)
    result = jsonable_encoder(t)
    return result