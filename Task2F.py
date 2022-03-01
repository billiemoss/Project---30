from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import datetime
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)

N = 5
dt = 2

at_risk_stations = stations_highest_rel_level(stations, N)

station_list = []
station_dates = []

for station in at_risk_stations:
    station_list.append(station.name)
    
for i in range(len(station_list)):
    station_plot = station_list[i]
    station_2 = at_risk_stations[i]
    dates, levels = fetch_measure_levels(station_2.measure_id, dt=timedelta(days=dt))
    plot_water_level_with_fit(station_plot, dates, levels, 4)