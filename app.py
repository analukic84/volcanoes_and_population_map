import folium
import pandas


data = pandas.read_csv("Volcanoes_world.txt", sep=";")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elevation = list(data["ELEV"])


def get_icon_color(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"


my_map = folium.Map(location=[40.00, -95.00],
                    width="100%",
                    height="100%",
                    zoom_start=4,
                    tiles="Stamen Terrain")

feature_group_v = folium.FeatureGroup(name="Volcanoes")

"""
# icon - location drop shape
for latitude, longitude, elev, name_v in zip(lat, lon, elevation, name):
    feature_group_v.add_child(folium.Marker(location=[latitude, longitude],
                                          popup=f"Elevation: {elev} m",
                                          tooltip=name_v,
                                          draggable=False,
                                          icon=folium.Icon(color=get_icon_color(elev))))
"""
# icon - circle shape with shadow
for latitude, longitude, elev, name_v in zip(lat, lon, elevation, name):
    feature_group_v.add_child(folium.CircleMarker(location=(latitude, longitude),
                                                  radius=8,
                                                  popup=f"Elevation: {elev} m",
                                                  tooltip=name_v,
                                                  color="grey",
                                                  weight=1,
                                                  fill_color=get_icon_color(elev),
                                                  fill_opacity=0.7,
                                                  fill=True))

feature_group_p = folium.FeatureGroup(name="Population")

feature_group_p.add_child(folium.GeoJson(data=open("Population_world_2005.json", "r", encoding="utf-8-sig").read(),
                                         style_function=lambda x: {
                                             "fillColor": "green"
                                             if x["properties"]["POP2005"] < 10000000
                                             else "orange" if 10000000 <= x["properties"]["POP2005"] < 40000000
                                             else "red"}))

my_map.add_child(feature_group_v)
my_map.add_child(feature_group_p)

my_map.add_child(folium.LayerControl(collapsed=False))
my_map.save("map_world_volcanoes.html")