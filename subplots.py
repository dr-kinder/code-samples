# subplot.py
# -------------------------------------------------------------------------
# Create four plots in the same figure using plt.subplots().
# ------------------------------------------------------------------------- 
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random

t = np.linspace(0, 1, 101)

# Create Figure and Axes objects.
fig, ax = plt.subplots(2,2)

# Use methods of Axes objects to add subplots.
ax[0,0].hist(random(20))                      # Upper left
ax[0,1].plot(t, t**2, t, t**3 - t)            # Upper right
ax[1,0].plot(random(20), random(20), 'r*')    # Lower left
ax[1,1].plot(t*np.cos(10*t), t*np.sin(10*t))  # Lower right
fig.suptitle("Data and Functions")            # Entire plot

plt.show()
