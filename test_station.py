# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create an arbitrary station  
   
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    
    
def test_inconsistent_typical_range_stations():
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    assert len(inconsistent_stations) > 0




def create_test_stations(n):

    # Create n arbitrary test stations
    stations = []
    for i in range(n):
        s_id = "s-id-" + str(i)
        m_id = "m-id-" + str(i)
        label = "station" + str(i)
        coord = (i*1.5, i*1.5)
        trange = (0, 100)
        river = "River X"
        town = "My Town"
        s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

        #Checking station created correctly, matches with above test for creation of single station:
        test_create_monitoring_station()

  
        stations.append(s) #Adding arbitrary station into a list

    return stations


station = create_test_stations(1)[0]
def test_relative_water_level():
    
    station.latest_level = 10
    

    assert station.relative_water_level() == 0.1

    #asserts that output of relative_water_level gives expected result when latest level = 10, range 0 to 100