# bar3d.py
# -------------------------------------------------------------------------
# Create a 3D "Lego plot" to illustrate the Central Limit Theorem.
# -------------------------------------------------------------------------
"""
Description
-----------

This script demonstrates the creation of a 3D bar chart and it illustrates how
the distribution of a sum of random numbers differs from the distribution those
numbers are drawn from.

The script will bin num_points random (x,y) pairs in a 2D histogram, then
display a 3D bar chart of this data.  Each x and y coordinate is the sum
of num_to_sum numbers drawn from the uniform random distribution on [0,1).

Adjust num_to_sum and use different random number generators to explore the
Central Limit Theorem.  (The Central Limit Theorem implies that the
distribution of the *sum* of many random numbers should approach a normal
distribution.)
"""
# %% Setup
import numpy as np
import matplotlib.pyplot as plt

# Create a random number generator.
rng = np.random.default_rng()  # create a random number generator object
rand = rng.random              # assign its uniform distribution method to rand

# Import the 3D plotter.
from mpl_toolkits.mplot3d import Axes3D

# %% Generate data and histogram.
# Generate random (x,y) pairs to bin.  Each coordinate is the sum of N numbers
# drawn from the uniform distribution on [0,1).
num_points = 10000
num_to_sum = 2
num_bins = 20

x_vals = rand((num_points, num_to_sum)).sum(1)
y_vals = rand((num_points, num_to_sum)).sum(1)

# Use histogram2d to get counts and bin locations.
counts, x_bins, y_bins = np.histogram2d(x_vals, y_vals, bins=num_bins)

# %% Transform data for plotting 3D bar chart.
# For 3D bar chart, we need starting (x,y,z) coordinates for each bar and
# (dx,dy,dz) to specify its shape.  The following code uses meshgrid, diff, and
# flatten to construct these inputs from the output of histogram2d.
x_start, y_start = np.meshgrid(x_bins[:-1], y_bins[:-1])
z_start = np.zeros_like(x_start)

x_length, y_length = np.meshgrid(np.diff(x_bins), np.diff(y_bins))
z_length = counts

x = x_start.flatten()
y = y_start.flatten()
z = z_start.flatten()
dx = x_length.flatten()
dy = y_length.flatten()
dz = z_length.flatten()

# %% Plot transformed data.
fig = plt.figure()
ax3d = Axes3D(fig)
ax3d.bar3d(x, y, z, dx, dy, dz)

plt.show()
