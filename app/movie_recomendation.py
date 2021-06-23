from fastapi import FastAPI
import recomandation
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Item(BaseModel):
    userid : int
    recomand : List[str] = []
    
    
    

@app.post("/items/{user_id}")
async def read_id(user_id: int):
    return recomandation.reco(user_id)







if __name__ == '__main__':
    uvicorn.run(app='test:app', reload=True, debug=True)