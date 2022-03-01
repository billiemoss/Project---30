from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)

    N = 5
    dt = 2
    p = 4
    highest_rel = stations_highest_rel_level(stations, N)
    for station in highest_rel:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, p)

if __name__ == "__main__":
    print("***Task 2F***")
    run()