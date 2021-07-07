# first_passage.py
# -------------------------------------------------------------------------
# Define a function to simulate first passage of a random walker.
# ------------------------------------------------------------------------- 
import numpy as np

def first_passage(N, L, p=0.5, message=False):
	"""
    Simulate a random walker that starts at the origin and takes steps to the
    right with probability p and to the left with probability 1-p.

	Return the number of steps for the first passage of location x==L,
	or give up after N steps and return np.nan.

	Use message=True to display the results on screen.
	"""
	rng = np.random.default_rng()     # create a random number generator
	dx = 2*(rng.random(N) < p) - 1    # generate individual steps
	x = np.cumsum(dx)                 # compute location after each step
	at_target = np.nonzero(x==L)[0]   # find indices where x == L

	if at_target.size > 0:
		n = at_target[0] + 1
		if message:
			print("First passage of x={} occurred after {} steps.".format(L, n))
		return n
	else:
		if message:
			print("Did not reach x={} after {} steps.".format(L, N))
		return np.nan
