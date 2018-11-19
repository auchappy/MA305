#!usr/bin/env python3
"""
==============================
Chapman, Piers - 05NOV18
Purpose: Use the trapezoidal rule to approximate the area of a curve
==============================
"""

import numpy as np
from matplotlib import pylab as plt
datM = np.loadtxt('dataM.txt',unpack=True)
lenM = len(datM)
datM = datM.astype(int)

print(datM)
