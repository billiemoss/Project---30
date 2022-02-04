from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_by_distance


"""Requirements for Task 1B"""

# Build list of stations
stations = build_station_list()

    #generates full stations by distance list
station_distances = stations_by_distance(stations, (52.2053, 0.1218))

    #indexes for first and last 10
first_10 = station_distances[:10]
last_10 = station_distances[-10:]

    #prints the output 
print(first_10)
print(last_10)


