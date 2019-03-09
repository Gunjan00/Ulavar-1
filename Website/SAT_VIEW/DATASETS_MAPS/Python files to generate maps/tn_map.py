import folium
import os
import pandas as pd

g_map= 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}'

m = folium.Map(location=[10.7905, 78.7047], zoom_start=7,
               tiles=g_map,
               attr='Google Map')
folium.TileLayer('Mapbox Control Room').add_to(m)
folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('Mapbox Bright').add_to(m)
folium.Marker([13.0827, 79.8707], popup=folium.Popup('<a href="map1.html" target="blank"><strong>Chennai</strong></a>'),icon=folium.Icon(icon='star')).add_to(m)


tn = os.path.join('tn_json.json')
rice = pd.read_csv('paddy.csv')

folium.Choropleth(
    geo_data= tn,
    name='Rice Production',
    data=rice,
    columns=['District', 'Area'],
    key_on='feature.properties.Dist_Name',
    fill_color='BuGn',
    fill_opacity=0.4,
    line_opacity=0.9,
    legend_name='Area in Hectares'
).add_to(m)
folium.LayerControl().add_to(m)
m.save('tn.html')
