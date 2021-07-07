# data_images.py
# -------------------------------------------------------------------------
# Illustrate differences between image and Cartesian coordinates.
# ------------------------------------------------------------------------- 
#%% Setup
import numpy as np
import matplotlib.pyplot as plt

# Define a coordinate grid.
# Same spacing, but twice as many points along x-axis
x_max, y_max = 2, 1
x_num, y_num = 200, 100

# Create coordinate arrays.
x = np.linspace(0,x_max,x_num)
y = np.linspace(0,y_max,y_num)

#%% Generate data to plot.
# Assign function values to placeholder array.
z = np.zeros((x_num,y_num))
for i in range(x_num):
	for j in range(y_num):
		z[i][j] = (x[i] - 2*y[j])**2

# Use meshgrid to generate the same function values.
X,Y = np.meshgrid(x,y)
Z = (X-2*Y)**2

#%% Visualize results.
fig, ax = plt.subplots(2,3, figsize=(12,6))
fig.suptitle(r"Plots of $f(x,y) = (x-2y)^2$")

ax[0,0].imshow(z)
ax[0,0].set_title("Loop: Image Coordinates")

ax[0,1].imshow(z, origin="lower")
ax[0,1].set_title("Loop: Spatial Coordinates")

ax[0,2].imshow(Z)
ax[0,2].set_title("meshgrid: Image Coordinates")

ax[1,0].imshow(z.transpose(), origin="lower")
ax[1,0].set_title("Loop: Transpose + Spatial Coordinates")

ax[1,1].imshow(Z, origin="lower")
ax[1,1].set_title("meshgrid: Spatial Coordinates")

ax[1,2].pcolormesh(X, Y, Z, shading='auto')
ax[1,2].axis('image')
ax[1,2].set_title("pcolormesh")

plt.show()
