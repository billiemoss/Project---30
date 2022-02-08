from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

sorted_inconsistent_stations = []
inconsistent_stations = []
stations = build_station_list()

range_stations = inconsistent_typical_range_stations(stations)
for station in inconsistent_typical_range_stations(stations):
    if inconsistent_typical_range_stations(station) == False:
        inconsistent_stations.append(station)

print(inconsistent_stations)
print("aa")
