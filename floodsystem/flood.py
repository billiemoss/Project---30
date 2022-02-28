from .station import MonitoringStation



#Task 2B - function which orders stations by relative water level

def stations_levels_over_threshold(stations, tol):
    output = []
    for station in stations:
        rel_level = station.relative_water_level()
        try:
            if rel_level > tol:
                output.append((station, station.relative_water_level()))
        except:
            pass
    return sorted(output, key=lambda x: x[0].relative_water_level(), reverse=True)



#Task 2C - function which returns ordered list of the N stations with highest relative level
def stations_highest_rel_level(stations, N):
    stations = [station for station in stations if station.relative_water_level() != None]
    return sorted(stations, key=lambda x: x.relative_water_level(), reverse=True)[:N]