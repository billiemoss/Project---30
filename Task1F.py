from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

sorted_inconsistent_stations = []
stations = build_station_list()
inconsistent_stations = inconsistent_typical_range_stations(stations)
for station in sorted(inconsistent_stations.items()):
  sorted_inconsistent_stations.append(station)


print(sorted_inconsistent_stations)
