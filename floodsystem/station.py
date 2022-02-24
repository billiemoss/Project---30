# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""
from .datafetcher import fetch_latest_water_level_data

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    #Task 1F - method to check high low range data for consistency
    def typical_range_consistent(self):
        if self.typical_range == None:
            return False
        low = float(self.typical_range[0])
        high =float(self.typical_range[1])
        if high < low:
            return False 
        else:
            return True
    
    #Task 2B - method to return latest water level as a fraction of the typical range
    def relative_water_level(self):

        current_level = fetch_latest_water_level_data()
        low = float(self.typical_range[0])
        high =float(self.typical_range[1])
        span = high - low
        level_above_low = current_level - low
        fraction = level_above_low / span
        if self.typical_range_consistent() == False:
            return None
        elif FileExistsError:
             return None
        else:
            return fraction

    


#given a list of station objects, returns a list of stations that have inconsistent data

def inconsistent_typical_range_stations(stations):
    
    inconsistent_data = []
    for station in stations:
        if station.typical_range_consistent() == False:
          inconsistent_data.append(station.name)
    return inconsistent_data



# MonitoringStation.typical_range_consistent

