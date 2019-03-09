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
rice = pd.read_csv('rice_prod.csv')


folium.Marker([10.3673, 77.9803], popup=folium.Popup('<a href="tn.html" target="blank"><strong>Tamil Nadu</strong></a>'),icon=folium.Icon(icon='star'), tooltip=tooltip).add_to(m)

#Color options---- BuGn, BuPu, GnBu, OrRd, PuBu, PuBuGn, PuRd, RdPu, YlGn, YlGnBu, YlOrBr, and YlOrRd

#Production

folium.Choropleth(
    geo_data=states,
    name='Production',
    data=rice,
    columns=['State', 'Avg_rice'],
    key_on='feature.properties.NAME_1',
    fill_color='YlGn',
    fill_opacity=0.4,
    line_opacity=0.9,
    legend_name='Production Rate (%)'
).add_to(m)

folium.LayerControl().add_to(m)
m.save('production.html')
