import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def polyfit(dates, levels, p):
    try:
        x = matplotlib.dates.date2num(dates)
        x0 = x[0]
        y = levels
        p_coeff = np.polyfit((x - x0),y,p)
        poly = np.poly1d(p_coeff)
        return poly, x0
    except:
        return False, False
    