# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

#Task 1B

#This function will return a list of (station name, town, distance) tuples
#Required input is stations (a list of the Monitoring Station objects), and the coordinate p(latitude, longitude)   
def stations_by_distance(stations, p):
   

   station_distance = []
   #calculate and append haversine distance to each object station in stations
   for station in stations:
      distance = haversine(station.coord, p)
      station_distance.append((station.name, station.town, distance))
   #sort stations by distance from coordinate p
   station_distance = sorted_by_key(station_distance, 2)
   return station_distance


#Task 1C

#This function will return a list of Station Names within a radius r of a coordinate x
#Required input is stations (a list of the Monitoring Station objects), and  the coordinate x(latitude, longitude), and the desired radius r(float)

def stations_within_radius(stations, x, r):

   stations_within_range_unsorted = []
   #calculate haversine distance to each object station in stations
   for station in stations:
      distance = haversine(station.coord, x)
      if distance <= r:
         stations_within_range_unsorted.append(station.name)
   
   return stations_within_range_unsorted

      
          
