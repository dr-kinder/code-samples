# data_dictionary.py
# -------------------------------------------------------------------------
# Store input and data two different simulations in a dictionary.
# This script requires first_passage.py to be in the same directory.
# -------------------------------------------------------------------------
from first_passage import first_passage

data = {}		# empty dictionary to store all data
data['A'] = {}  # empty dictionary within data to store Simulation A
data['B'] = {}  # empty dictionary within data to store Simulation B

#%% Define and run simulations.
samples = 500

data['A']['input'] = dict(N=1000, L=10, p=0.5)
data['A']['results'] = \
	[ first_passage(**data['A']['input']) for n in range(samples) ]

data['B']['input'] = dict(N=1000, L=20, p=0.5)
data['B']['results'] = \
	[ first_passage(**data['B']['input']) for n in range(samples) ]

#%% Run more simulations.  Use "+=" to append new list to old.
data['A']['results'] += \
	[ first_passage(**data['A']['input']) for n in range(samples) ]

data['B']['results'] += \
	[ first_passage(**data['B']['input']) for n in range(samples) ]
