# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_by_distance(stations, p):
   

   station_distance = []
   for station in stations:
      distance = haversine(station.coord, p)
      station_distance.append((station.name, station.town, distance))
   #sort by distance
   station_distance = sorted_by_key(station_distance, 2)
   return station_distance
