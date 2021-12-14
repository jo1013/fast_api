import csv
import pandas as pd
import folium
import uvicorn
import os

from typing import Optional
from fastapi import FastAPI
from bs4 import BeautifulSoup

from fastapi.responses import HTMLResponse

    
    
    
##  ----------------------------------------------------------------------##    
### 경로


# 현재 스크립트 경로
dire = os.path.dirname(os.path.abspath( __file__ ))
# 상위 디렉토리
par_dir = os.path.abspath(os.path.join(dire, os.pardir))

data_dir = par_dir + '/data'

html_dir = par_dir + '/html'

map_html = html_dir + "/map.html"




##  ----------------------------------------------------------------------##
# 맵 folium상에 폴리곤 표시 및 저장


motor_acc = pd.read_csv(data_dir + '/17_19_motorcycle_위치정보.csv', encoding='UTF-8')



seoul_location = motor_acc[['위도', '경도']]

map = folium.Map(location =  [37.5642,127.0016985,], zoom_start =12)

for a in seoul_location.index:
    latitude = seoul_location.loc[a,"위도"]
    longtitude = seoul_location.loc[a,"경도"]
    tooltip = "사고!"
    folium.Marker([latitude, longtitude], popup = '<i>위험</i>', tooltip =tooltip).add_to(map)

map.save(map_html)


##  ----------------------------------------------------------------------##



#FAST API 구현


app = FastAPI()




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}




@app.get("/")
async def map():
    content = open(map_html, "r", encoding="utf8")
    content = BeautifulSoup(content, 'html.parser')
    return HTMLResponse(content = content, status_code=200)








if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)