from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
import numpy as np

def test_polyfit():
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.name == "Cam":
            dates,levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=2))
            assert len(dates) == len(levels)

            if dates == [] or levels == []:
                pass
            else:
                poly, d0 = polyfit(dates, levels, 4)
                assert isinstance(poly, np.poly1d)
                assert isinstance(d0, float)

            