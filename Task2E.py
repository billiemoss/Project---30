import datetime
from datetime import datetime 
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list

stations = build_station_list()
dt = 10
station_name = "Cam"
station_cam = None
for station in stations:
    if station.name == station_name:
        station_cam = station
        break
dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))

date_time_str = dates
datetime_obj = datetime. strftime(date_time_str, '%d/%m/%y %H:%M:%S')


print(plot_water_levels("Cam",  dates, levels))

