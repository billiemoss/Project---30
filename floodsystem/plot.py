import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
from numpy import polyfit
import numpy as np


def plot_water_levels(station, dates, levels):
    t = []
    l = []  
    x, y = station.typical_range
    for date, level in zip(dates,levels):
        t.append(date)
        l.append(level)
    if len(t) == 0:
        return print("There isn't enough historic data for this station:", station.name)
    elif len(l) == 0:
        return print("There isn't enough historic data for this station:", station.name)
    else:
        plt.plot(t, l)
        plt.plot([t[0],t[-1]], [x,x])
        plt.plot([t[0],t[-1]], [y,y])
        plt.gcf().autofmt_xdate()
        #adds axis labels
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        #rotates date labels
        plt.xticks(rotation=45)
        #adds plot title
        plt.title(station.name)
        #makes sure plot doesnt cut off date labels
        plt.tight_layout()
        #display plot
        plt.show()



def plot_water_level_with_fit(station, dates, levels, p):
    t = []
    l = []  
    x, y = station.typical_range
    y= polyfit(dates, levels, p)
    a = y[0]
    b = y[1]
    for date, level in zip(dates,levels):
        t.append(date)
        l.append(level)
    if len(t) == 0:
        return print("There isn't enough historic data for this station:", station.name)
    elif len(l) == 0:
        return print("There isn't enough historic data for this station:", station.name)
    else:
        plt.plot(t, l)
        plt.plot([t[0],t[-1]], [x,x])
        plt.plot([t[0],t[-1]], [y,y])
        x1 = np.linspace(t[0], t[-1], 30)
        plt.plot(x1, a(x1))
        plt.gcf().autofmt_xdate()
        #adds axis labels
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        #rotates date labels
        plt.xticks(rotation=45)
        #adds plot title
        plt.title(station.name)
        #makes sure plot doesnt cut off date labels
        plt.tight_layout()
        #display plot
        plt.show()
