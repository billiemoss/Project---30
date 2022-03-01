import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
from numpy import polyfit

def plot_water_levels(station, dates, levels):
    t = []
    l = []  
    low_range = []
    high_range = []
    for date, level in zip(dates,levels):
        t.append(date)
        l.append(level)
    if len(t) == 0:
        return print("There isn't enough historic data for this station")
    elif len(l) == 0:
        return print("There isn't enough historic data for this station")
    else:
        plt.plot(t, l)
        plt.gcf().autofmt_xdate()
        #adds axis labels
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        #rotates date labels
        plt.xticks(rotation=45, )
        #adds plot title
        plt.title(station.name)
        #makes sure plot doesnt cut off date labels
        plt.tight_layout()
        #display plot
        plt.show()



def plot_water_level_with_fit(station, dates, levels, p):
    t = []
    l = []  
    q = []
    try:
        for date, level in zip(dates, levels):
            t.append(date)
            t.append(level)
        x, y  = polyfit(dates, levels, p)
        for level in x:
            q.append(level)
        #plots the data
        plt.plot(t, l)
        plt.plot(y,q)
        #adds axis labels
        plt.xlabel('polyfit')
        plt.ylabel('water level (m)')
        #adds plot title
        plt.title(station)
        #makes sure plot doesnt cut off date labels
        plt.tight_layout()
        #display plot
        plt.show()
    except:
        return False

