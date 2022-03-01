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

for station in stations_highest_rel_level(stations, N):
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
    date_time_str = dates
    datetime_obj = []
    for i in range(len(date_time_str)):
        datetime_obj.append(datetime. strftime(date_time_str[i], '%d/%m/%y %H:%M:%S'))
        
    print(plot_water_level_with_fit(station, datetime_obj, levels,4))

