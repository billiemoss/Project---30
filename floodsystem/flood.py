from station import MonitoringStation



#Task 2B - function which orders stations by relative water level
def stations_level_over_threshold(stations, tol):
    list_of_stations_over_threshold = []
    for station in stations:
        if tol <= MonitoringStation().relative_water_level() and MonitoringStation().typical_range_consistent() == True:
            list_of_stations_over_threshold.append(MonitoringStation.name, MonitoringStation().relative_water_level())
    sorted_list_of_stations_over_threshold = sorted(list_of_stations_over_threshold, key=lambda tup: tup[1], reverse=True)
    return sorted_list_of_stations_over_threshold



