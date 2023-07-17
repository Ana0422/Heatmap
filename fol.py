from folium import plugins
import folium
import pandas as pd
df = pd.read_csv('train.csv')


stationArr = df[['Y', 'X']].values

m = folium.Map(location=[stationArr[0][0], stationArr[0][1]], zoom_start=12)
m.add_child(plugins.HeatMap(stationArr[:50000], radius=15))
m.save('abc.html')
