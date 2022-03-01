from floodsystem.flood import stations_levels_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)
severe_risk = []
high_risk = []
moderate_risk = []
low_risk = []
threshold_for_severe = 2
threshold_for_high = 1
threshold_for_moderate = 0.8
threshold_for_low = 0.5

#evaluate risk by comparing to relative levels

def run():
    stations_severe = stations_levels_over_threshold(stations, threshold_for_severe)
    for station, level in stations_severe:
        severe_risk.append(station.name)
    print()
    print('Stations at Severe Risk of Flooding:', severe_risk)
    
    stations_high = stations_levels_over_threshold(stations, threshold_for_high)
    for station, level in stations_high:
        high_risk.append(station.name)
    print()
    print('Stations at High Risk of Flooding:', high_risk)

    stations_moderate = stations_levels_over_threshold(stations, threshold_for_moderate)
    for station, level in stations_moderate:
        moderate_risk.append(station.name)
    print()
    print('Stations at Moderate Risk of Flooding:', moderate_risk)

    stations_low = stations_levels_over_threshold(stations, threshold_for_low)
    for station, level in stations_low:
        low_risk.append(station.name)
    print()
    print('Stations at Low Risk of Flooding:', low_risk)


if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()

    


#evaluate risk by looking at the trend of water levels - using polynomial