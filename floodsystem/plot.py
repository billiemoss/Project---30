import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
from numpy import polyfit
import numpy as np
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels


def plot_water_levels(station, dates, levels):
    t = []
    l = []  
    dt = 10
    x, y = station.typical_range
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
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
    dt = 2
    try:
        best_fit_poly, d0 = polyfit(dates, levels, p)
    except:
        pass
    else: 
        a = matplotlib.dates.date2num(dates) - d0
        plt.plot(dates, best_fit_poly(a))

    x, y = station.typical_range
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
    w = polyfit(dates, levels, p)
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
        #adds axis labels
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        #rotates date labels
        plt.xticks(rotation=45)
        #adds plot title
        plt.title(station.name)
        plt.legend()
        #makes sure plot doesnt cut off date labels
        plt.tight_layout()
        #display plot
        plt.show()
