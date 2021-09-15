import json
import folium
import pandas

df = pandas.read_csv("volcanoes.txt",sep = ",")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])
name = list(df["NAME"])

def color_producer(elevation):
    if elevation<1000:
        return "green"
    elif 1000<= elevation <3000:
        return "orange"
    else:
        return "red"
 

map = folium.Map(location= [37.779052, -115.146502], zoom_start= 6,tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name= "Volcanoes")
for lt,ln,elv in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location= [lt,ln], popup = str(elv)+"m", radius= 6, color = "gray", fill_opacity = 0.7, fill_color = color_producer(elv)))
   

fg = folium.FeatureGroup(name= "Population")
fg.add_child(folium.GeoJson(data = (open('world.json','r', encoding='utf-8-sig').read()),style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005']< 10000000 else 'yellow' if 10000000<= x['properties']['POP2005']< 20000000 else 'red'} ))

map.add_child(fg)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Map.html")
print("Done")