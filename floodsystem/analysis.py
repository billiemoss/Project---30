import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates


def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    x_shifted = [n-x[0] for n in x]
    p_coeff = np.polyfit(x_shifted, levels , p)
    poly = np.poly1d(p_coeff)

    return poly(x_shifted), x_shifted