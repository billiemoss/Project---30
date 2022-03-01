import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates


def polyfit(dates, levels, p):
    x = []
    x.append(matplotlib.dates.date2num(dates))
    p_coeff = np.polyfit(x - x[0], levels , p)
    poly = np.poly1d(p_coeff)
    return poly, x[0]