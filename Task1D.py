from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

#how many rivers have at least one monitoring station
stations = build_station_list()
number_of_stations = len(rivers_with_station(stations))
print (number_of_stations)

#first ten rivers with stations in alphabetical order
ordered_rivers = sorted(rivers_with_station(stations))
print(ordered_rivers[0:10])


#stations on River Aire in alphabetical order
river_stations = stations_by_river(stations)
aire_stations = river_stations['River Aire']
ordered_aire_stations = sorted(aire_stations)
print(ordered_aire_stations)

#stations on River Cam in alphabetical order
cam_stations = river_stations['River Cam']
ordered_cam_stations = sorted(cam_stations)
print(ordered_cam_stations)

#stations on River Thames in alphabetical order
thames_stations = river_stations['River Thames']
ordered_thames_stations = sorted(thames_stations)
print(ordered_thames_stations)