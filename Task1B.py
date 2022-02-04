from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_by_distance


"""Requirements for Task 1B"""

# Build the list of stations
stations = build_station_list()

    #Use this list as the input for distance calculating and sorting function
station_distances = stations_by_distance(stations, (52.2053, 0.1218))

    #indexes for first and last 10 (sorted by distance)
closest_10 = station_distances[:10]
furthest_10 = station_distances[-10:]

    #prints the output 
print(closest_10)
print(furthest_10)


