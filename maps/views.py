from django.shortcuts import render
import folium

def index(request):
    bukhara = [39.76774304215008, 64.4545480125641]
    qarshi = [38.86114121433274, 65.7863067220425]
    tosh = [41.297781163801055, 69.24195263149142]
    m = folium.Map(bukhara, zoom_start=7)
    
    group_1 = folium.FeatureGroup("first group").add_to(m)
    folium.Marker(bukhara,tooltip="Buxoro", icon=folium.Icon("red")).add_to(group_1)
    folium.Marker(qarshi,tooltip="Qarshi", icon=folium.Icon("red")).add_to(group_1)
    
    group_2 = folium.FeatureGroup("second group").add_to(m)
    folium.Marker(tosh,tooltip="Toshkent", icon=folium.Icon("green")).add_to(group_2)
    
    folium.LayerControl().add_to(m)
    trail_coordinates = [
        bukhara,
        qarshi,
        tosh
    ]
    
    folium.PolyLine(trail_coordinates, tooltip="Yol").add_to(m)
    context = {'map': m._repr_html_()}
    return render(request,'index.html',context)