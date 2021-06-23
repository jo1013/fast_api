from fastapi import FastAPI
import recomandation
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


class Item(BaseModel):
    userid : int
    recomand : List[str] = []
    
    
@app.get("/")
async def read_root():
    return {"Hello": "World"}
    

@app.get("/items/{user_id}")
async def read_id(user_id: int):
    t = recomandation.reco(user_id)
    result = jsonable_encoder(t)
#    return result
    return result
   # return recomandation.reco(user_id)







# if __name__ == '__main__':
#     uvicorn.run(app='test:app', reload=True, debug=True)