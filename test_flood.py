from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_levels_over_threshold, stations_highest_rel_level

def create_test_stations(n):

#create an arbitary list of stations to be tested

    stations = []
    
    for i in range(n):
        s_id = "s-id-" + str(i)
        m_id = "m-id-" + str(i)
        label = "station" + str(i)
        coord = (i*1.5, i*1.5)
        trange = (0,10)
        river = "River-id" + str(i)
        town = "Town-id" + str(i)
        s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

        stations.append(s)
    
    return stations


def test_stations_over_threshold():

    threshold = 0.7

    stations = create_test_stations(7)
    stations[0].latest_level = None #Test for operation with unavilable data
    stations[1].latest_level = 4
    stations[2].latest_level = 6
    stations[3].latest_level = 5
    stations[4].latest_level = 3
    stations[5].latest_level = 10.5
    stations[6].latest_level = 2

    stations[1].typical_range = (1.5, 1) #Test for operation with inconsistent range

    result = stations_levels_over_threshold(stations, threshold)

    assert result == sorted(result, key=lambda x: x[0].relative_water_level(), reverse=True) 
    #Asserts that result is as expected, ie function successfully sorts stations by water level

    

def test_stations_highest_rel_level():

    stations = create_test_stations(7)
    stations[0].latest_level = None #Test for operation with unavilable data
    stations[1].latest_level = 4
    stations[2].latest_level = 6
    stations[3].latest_level = 5
    stations[4].latest_level = 3
    stations[5].latest_level = 10.5
    stations[6].latest_level = 2

    stations[1].typical_range = (1.5, 1) #Test for operation with inconsistent range

    result = stations_highest_rel_level(stations, 5)

    assert result == sorted(result, key=lambda x: x.relative_water_level(), reverse=True)
    assert len(result) == 5

    #Asserts that result is as expected, ie function successfully sorts station by relative water level and keeps N highest
