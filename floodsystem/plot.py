import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    t = []
    l = []  
    for date, level in zip(dates,levels):
        print(date, level)
        t.append(date)
        print(t)
        l.append(level)
    #plots the data
    plt.plot(t, l)
    #adds axis labels
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    #rotates date labels
    plt.xticks(rotation=45);
    #adds plot title
    plt.title(station)
    #makes sure plot doesnt cut off date labels
    plt.tight_layout()
    #display plot
    plt.show()
    


def plot_water_level_with_fit(station, dates, levels, p):
    print()

