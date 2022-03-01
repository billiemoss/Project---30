from floodsystem.flood import stations_levels_over_threshold
from floodsystem.stationdata import build_station_list

stations = build_station_list()
severe_risk = []
high_risk = []
moderate_risk = []
low_risk = []

#evaluate risk by comparing to relative levels
y = stations_levels_over_threshold(stations, 0.8)

for station in stations_levels_over_threshold(stations, 0.8):
    severe_risk.append(station.name)

print (severe_risk)

#evaluate risk by looking at the trend of water levels - using polynomial