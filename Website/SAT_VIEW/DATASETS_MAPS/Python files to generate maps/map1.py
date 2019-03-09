import folium
import geocoder
import pandas as pd

df_shops= pd.read_csv('shops.csv')

#Farming shops

X1= df_shops.iloc[:,1].values
Y1= df_shops.iloc[:,3].values
shop= df_shops.iloc[:,0].values
print(X1)

tooltip='Click for more info'
m = folium.Map(location=[13.0827, 80.2707], zoom_start=12)

for lt,lg,sp in zip(X1,Y1,shop):
    folium.Marker([lt, lg],
                  popup= sp,
                  icon=folium.Icon(color='green',icon='leaf'),
                  tooltip=tooltip).add_to(m)
#Banks

df_shops= pd.read_csv('banks.csv')
X2= df_shops.iloc[:,1].values
Y2= df_shops.iloc[:,2].values
bank= df_shops.iloc[:,0].values


for lt,lg,sp in zip(X2,Y2,bank):
    folium.Marker([lt, lg],
                  popup= sp,
                  icon=folium.Icon(icon='home'),
                  tooltip=tooltip).add_to(m)

m.save('map1.html')