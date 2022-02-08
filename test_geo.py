
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number 
from floodsystem.stationdata import build_station_list

#Task 1B Test


def test_stations_by_distance():
    stations = build_station_list()
    station_distances = stations_by_distance(stations, (52.2053, 0.1218))

    assert round(station_distances[0][2], 2) == 0.84


#Task 1C Test

def test_stations_within_radius():
    stations = build_station_list()
    stations_in_range = stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert len(stations_in_range)>0


#Task 1D Test

def test_rivers_by_station_number():
    stations = build_station_list()
    number_of_rivers_output = rivers_by_station_number(stations, 4)

    assert len(number_of_rivers_output) >= 4