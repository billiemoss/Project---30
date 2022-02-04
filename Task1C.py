from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_within_radius


"""Requirements for Task 1C"""

# Build the list of stations
stations = build_station_list()

#Use this list as the input for the range checking function

stations_within_range_unsorted = stations_within_radius(stations, (52.2053, 0.1218), 10)

#sort the unsorted list alphabetically and print result

stations_within_range_sorted = sorted(stations_within_range_unsorted)

print(stations_within_range_sorted)