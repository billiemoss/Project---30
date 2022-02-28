from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level




def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    #Specify the number of stations to be displayed
    N = 10

    at_risk_stations = stations_highest_rel_level(stations, N)
    for station in at_risk_stations:
        if station.relative_water_level() < 100:
            print(station.name, station.relative_water_level())

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()

