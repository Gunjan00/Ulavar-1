import folium
import os
import pandas as pd

g_map= 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}'
m = folium.Map(location=[22.5937, 78.9629], zoom_start=5,
               tiles=g_map,
               attr='Google Map'
               )

states = os.path.join('india_state.json')
new= pd.read_csv('rainfall.csv')
folium.TileLayer('Mapbox Control Room').add_to(m)
folium.TileLayer('openstreetmap').add_to(m)

#New

folium.Choropleth(
    geo_data=states,
    name='Annual Rainfall in mm',
    data=new,
    columns=['State', 'rainfall'],
    key_on='feature.properties.NAME_1',
    fill_color='BuPu',
    fill_opacity=0.4,
    line_opacity=0.9,
    legend_name='Annual Rainfall in mm'
).add_to(m)


folium.LayerControl().add_to(m)

m.save('rainfall.html')