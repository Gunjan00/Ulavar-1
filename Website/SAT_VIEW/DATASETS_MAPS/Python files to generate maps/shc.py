import folium
import os
import pandas as pd

g_map= 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}'

tooltip = 'Tamil Nadu' + \
          '; Total Districts=33' + \
          '; production=5675.7 thousand tonne'

m = folium.Map(location=[22.5937, 78.9629], zoom_start=5,
               tiles=g_map,
               attr='Google Map')
folium.TileLayer('Mapbox Control Room').add_to(m)
folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('Mapbox Bright').add_to(m)

states = os.path.join('india_state.json')
ph= pd.read_csv('Ph.csv')
P= pd.read_csv('phosphorus.csv')
K= pd.read_csv('potassium.csv')
N= pd.read_csv('nitrogen.csv')

folium.Marker([10.3673, 77.9803], popup=folium.Popup('<a href="tn.html" target="blank"><strong>Tamil Nadu</strong></a>'),icon=folium.Icon(icon='star'), tooltip=tooltip).add_to(m)

#Ph

folium.Choropleth(
    geo_data=states,
    name='pH',
    data=ph,
    columns=['State', 'ph'],
    key_on='feature.properties.NAME_1',
    fill_color='PuRd',
    fill_opacity=0.4,
    line_opacity=0.9,
    legend_name='pH of areas',
).add_to(m)

#Nitrogen

folium.Choropleth(
    geo_data=states,
    name='Nitrogen',
    data=N,
    columns=['State', 'Nitrogen'],
    key_on='feature.properties.NAME_1',
    fill_color='OrRd',
    fill_opacity=0.4,
    line_opacity=0.9,
    legend_name='Nitrogen',
    show=False

).add_to(m)

#Potassium

folium.Choropleth(
    geo_data=states,
    name='Potassium',
    data=K,
    columns=['State', 'potassium'],
    key_on='feature.properties.NAME_1',
    fill_color='GnBu',
    fill_opacity=0.4,
    line_opacity=0.9,
    legend_name='Potassium',
    show=False

).add_to(m)

#Phosphorus

folium.Choropleth(
    geo_data=states,
    name='Phosphorus',
    data=P,
    columns=['State', 'Phosphorus'],
    key_on='feature.properties.NAME_1',
    fill_color='YlOrBr',
    fill_opacity=0.4,
    line_opacity=0.9,
    legend_name='Phosphorus',
    show=False

).add_to(m)


folium.LayerControl().add_to(m)
m.save('Nutrients.html')
