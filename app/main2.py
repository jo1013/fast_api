import requests
import json
import csv
import pandas as pd
import folium
import webbrowser
import uvicorn


from matplotlib import pyplot
from sklearn.base import BaseEstimator, TransformerMixin
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from folium.plugins import MarkerCluster
from bs4 import BeautifulSoup


motor_acc = pd.read_csv('17_19_motorcycle.csv',encoding='cp949')


seoul_location = motor_acc[['위도', '경도']]

map = folium.Map(location =  [37.5642,127.0016985,], zoom_start =12)

for a in seoul_location.index:
    latitude = seoul_location.loc[a,"위도"]
    longtitude = seoul_location.loc[a,"경도"]
    tooltip = "사고!"
    folium.Marker([latitude, longtitude], popup = '<i>위험</i>', tooltip =tooltip).add_to(map)

map.save('map.html')





app = FastAPI()







f = open("map.html", "r", encoding="utf8")
soup = BeautifulSoup(f, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))

filepath = "map.html"

@app.get("/")
def abc():
    f = open("map.html", "r", encoding="utf8")




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)