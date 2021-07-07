# vortex.py  
# -------------------------------------------------------------------------
# Create a quiver plot.
# ------------------------------------------------------------------------- 
import numpy as np
import matplotlib.pyplot as plt

coords = np.linspace(-1, 1, 11)
X, Y = np.meshgrid(coords, coords)
Vx, Vy = Y, -X

plt.figure()
# pivot='mid' places centers of arrows on grid points
plt.quiver(X, Y, Vx, Vy, pivot='mid')
plt.axis('square')
plt.show()
