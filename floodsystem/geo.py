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



#Task 1E

#This function will return a list of tuples of form (river name, number of stations)
#The N rivers with the greatest number of stations will be included - as well as overflow for multiple stations with the same number at N

#Required input is stations (a list of the Monitioring Station objects), and the number of stations to be included, N - remember overflow case

def rivers_by_station_number(stations, N):

#Create a list of all the river names, with repeated entries for rivers with multiple stations
  
   list_of_river_names = []
   for station in stations:
      river_name = station.river
      list_of_river_names.append(river_name)
   
#Turn this list into a list of tuples of the form (river name, number of stations on that river)

   river_number_of_stations = []
   for i in list_of_river_names:
      river_number_of_stations.append((i, list_of_river_names.count(i)))

#Remove duplicates from the above list of tuples

   river_number_of_stations_unique = []
   for i in river_number_of_stations:
      if i not in river_number_of_stations_unique:
         river_number_of_stations_unique.append(i)

#Sort this list by the number of stations


   rivers_sorted_by_station_number_unclipped = sorted_by_key(river_number_of_stations_unique, 1)

 
   number_of_stations_list = []
  

  #Remove entries in the list which have fewer stations than the Nth highest entry

   for i in rivers_sorted_by_station_number_unclipped:
      number_of_stations = i[1]
      number_of_stations_list.append(number_of_stations)



   qualifying_number_of_stations = number_of_stations_list[-N]


   rivers_sorted_by_station_number_clipped = []
   for i in rivers_sorted_by_station_number_unclipped:
      if i[1] >= qualifying_number_of_stations:
         rivers_sorted_by_station_number_clipped.append(i)



   return rivers_sorted_by_station_number_clipped


