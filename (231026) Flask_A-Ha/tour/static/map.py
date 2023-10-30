import folium
import pandas as pd
 
def map(tour):
    data=pd.read_csv('../../data_2.csv')
    tour_loc = (data[data['관광지']==tour].iloc[0]['latitude'], data[data['관광지']==tour].iloc[0]['longitude']) 
    m = folium.Map(location=[tour_loc[0], tour_loc[1]], zoom_start=12)
    folium.Marker(location=tour_loc, tooltip=tour).add_to(m)
    m.save('map.html')

map(tour)