import datetime
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation


stations = build_station_list()
update_water_levels(stations)

#retrieve the stations with the highest relative water levels


dt = 10

for station in stations_highest_rel_level(stations, 5):
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
    date_time_str = dates
    datetime_obj = []
    for i in range(len(date_time_str)):
        datetime_obj.append(datetime. strftime(date_time_str[i], '%d/%m/%y %H:%M:%S'))
        
    print(plot_water_levels(station, datetime_obj, levels))





