# nd_random_walks.py
# -------------------------------------------------------------------------
# Class to simulate various random walks in N dimensions.
# ------------------------------------------------------------------------- 
"""
Description
-----------

This module implements several N-dimensional random walks.

Each RandomWalk class has these standard methods:
	- get_walk(N)        --> N steps in a random walk
	- get_endpoints(M,N) --> endpoints from M walks of N steps
	- get_distances(M,N) --> final distances from M walks of N steps

The class hierarchy is as follows.

RandomWalk -- general random walk class
	LatticeWalk     --  random walk on a D-dimensional lattice
					    default is a cubic lattice in D dimensions
		TriangularWalk  -- 2D triangular lattice
		HoneycombWalk   -- 2D honeycomb lattice
	DirectionalWalk --  random walks of variable step size in D dimensions
				        defaults to constant step length in random directions
		UniformWalk     -- step size drawn from uniform distribution
		GaussianWalk    -- step size drawn from normal distribution
		ExponentialWalk -- step size drawn from exponential distribution
		ParetoWalk      -- step size drawn from power law distribution
"""
import numpy as np

class RandomWalk():
	def __init__(self, dimension=1):
		# Create a random number generator.
		self.rng = np.random.default_rng()
		# Store dimension and starting point internally.
		self.D = dimension
		self.r0 = np.zeros((self.D,1))

	def _get_steps(self,N):
		# Internal method.  Generate individual steps of the random walk.
		return np.zeros((self.D, N))   # placeholder for parent class
	
	def get_walk(self,N):
		return np.append(self.r0, np.cumsum(self._get_steps(N), 1), axis=1)

	def get_endpoints(self,M,N):
		return np.array([self.get_walk(N)[:,-1] for m in range(M)]).transpose()

	def get_distances(self,M,N):
		return np.sqrt(np.sum(self.get_endpoints(M,N)**2, axis=0))


class LatticeWalk(RandomWalk):
	def __init__(self, dimension=1):
		super().__init__(dimension)
		# Create list of legal steps on D-dimensional cubic lattice.
		M = np.eye(self.D)
		self.basis = [M[:,n] for n in range(self.D)]
		self.basis += [-M[:,n] for n in range(self.D)]

	def _get_steps(self, N):
		# Generate individual steps by randomly choosing from self.basis.
		return self.rng.choice(self.basis, size=N).transpose()


class TriangularWalk(LatticeWalk):
	def __init__(self, dimension=2):
		super().__init__(dimension=2)
		# Create list of legal steps on a triangular lattice:
        # unit vector along x-axis, plus images under successive rotations.
		cosTheta, sinTheta = np.cos(np.pi/3), np.sin(np.pi/3)
		R = np.array([[cosTheta, -sinTheta], [sinTheta, cosTheta]])
		v = np.array([0,1])
		self.basis = []
		for n in range(6):
			self.basis += [v]
			v = np.dot(R,v) 


class HoneycombWalk(LatticeWalk):
	def __init__(self, dimension=2):
		super().__init__(dimension=2)
		# Create list of legal steps on a triangular lattice:
        # unit vector along x-axis, plus images under successive rotations
        # generates on sublattice.  _get_steps() accounts for the other.
		cosTheta, sinTheta = np.cos(2*np.pi/3), np.sin(2*np.pi/3)
		R = np.array([[cosTheta, -sinTheta], [sinTheta, cosTheta]])
		v = np.array([0,1])
		self.basis = []
		for n in range(3):
			self.basis += [v]
			v = np.dot(R,v) 

	def _get_steps(self, N):
		# Honeycomb lattice has two sublattices.  (-1)**n accounts for this:
        # Rotate step by 180 degrees if on sublattice B.
		return self.rng.choice(self.basis, size=N).T * (-1)**np.arange(N)


class DirectionalWalk(RandomWalk):
	def _direction(self, N):
		# Use the Box-Muller transform to generate N random unit vectors.
		vectors = self.rng.normal(size=(self.D,N))
		lengths = np.sqrt(np.sum(vectors**2,0))
		return vectors/lengths

	def _magnitude(self, N):
		# Only directions are random for this class.  Step size is 1.
		return np.ones(N)

	def _get_steps(self, N):
		# Return steps for random walk of N steps in D dimensions.
		return self._direction(N) * self._magnitude(N)


class UniformWalk(DirectionalWalk):
	def _magnitude(self, N):
		# Draw N step sizes from the uniform distribution.  Mean size is 1.
		return 2*self.rng.random(size=N)


class GaussianWalk(DirectionalWalk):
	def _magnitude(self, N):
		# Draw N step sizes from chi distribution.  Mean size is 1.
		return np.sqrt(self.rng.chisquare(df=self.D, size=N)/self.D)


class ExponentialWalk(DirectionalWalk):
	def _magnitude(self, N):
		# Draw N steps from exponential distribution.  Mean size is 1.
		return self.rng.exponential(size=N)


class ParetoWalk(DirectionalWalk):
	def __init__(self, dimension=1, nu=2):
		super().__init__(dimension)
        # Exponent and normalization factor for power law distribution.
		self.nu = nu
		self.norm = max(0.01, nu-1)

	def _magnitude(self, N):
		# Draw N step sizes from Pareto distribution.  Mean is 1 if nu > 1.01.
		return self.rng.pareto(a=self.nu, size=N) * self.norm
