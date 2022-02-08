from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()

# builds a list of all stations with inconsistent typical range data
inconsistent_range_data = []
inconsistent_range_data = inconsistent_typical_range_stations(stations)
    
print(sorted(inconsistent_range_data))

