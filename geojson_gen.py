from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import pandas as pd
import folium.plugins
import IP2Location

url = 'https://github.com/firehol/blocklist-ipsets'
ext2 = 'netset'
ext1 = 'ipset'
ext3 = 'https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/'
counter = 0
allo=[]
IP2LocObj = IP2Location.IP2Location()
IP2LocObj.open("IP2LOCATION-LITE-DB5_1.BIN")
marker_locations=[]
marker_name=[]

def listf(url,ext = ''):
    page = requests.get(url).text
    soup = BeautifulSoup(page,'html.parser')
    return ['https://raw.githubusercontent.com' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

for file in listf(url, ext2):
    counter = counter +1
    file = file.replace('/blob','')
    print(file)
    df = pd.read_csv(file,sep=";",index_col=False)
    for rows in df.iterrows():
        if '#' not in rows[1][0]:
            rows[1][0] =rows[1][0].split("/")[0]
            file.replace(ext3,'')
            
            allo.append((IP2LocObj.get_all(rows[1][0]),rows[1][0],file))
            
            marker_locations.append((IP2LocObj.get_all(rows[1][0]).latitude,IP2LocObj.get_all(rows[1][0]).longitude))
counter =0
for file in listf(url, ext1):
    if (counter == 0):
        counter = 1
        continue
    file = file.replace('/blob','')
    print(file)
    df = pd.read_csv(file,sep="OFI",index_col=False)
    for rows in df.iterrows():  
        if '#' not in rows[1][0]:  
            
             allo.append((IP2LocObj.get_all(rows[1][0]),rows[1][0],file))             
import geopandas
import mapboxgl
from geojson import Point,FeatureCollection,Feature
features = []
x = 0
scalerank = 1
for i in allo:
    point = Point (([i[0].longitude,i[0].latitude]))
    features.append(({
      "type": "Feature",
      "properties": {
        "scalerank": scalerank,
        "name": i[0].ip,
        "comment": "haha",
        "name_alt": i[0].ip,
        "lat_y": i[0].latitude,
        "long_x": i[0].longitude,
        "region": i[0].region,
        "subregion": i[0].city,
        "featureclass": ""
      },
      "geometry": {
        "type": "Point",
        "coordinates": [i[0].longitude, i[0].latitude]
      }
    }))
    x = x +1
    if x == 100000:
        break
   
feature_collection = FeatureCollection(features)
with open('./SUPERCLUSTER/TEXT/FIXTURES/places.json', 'w') as f: #edit your  path
   json.dump(feature_collection,f,indent=4)        
           
