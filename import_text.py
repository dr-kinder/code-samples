# import_text.py
# -------------------------------------------------------------------------
# Load data from a text file by reading the file line by line.
# This script requires the data set 01HIVseries/HIVseries.csv.
# ------------------------------------------------------------------------- 
import numpy as np

f = open("HIVseries.csv")
temp_data = []

for line in f:
	print(line)
	x,y = line.split(',')
	temp_data += [ (float(x), float(y)) ]

f.close()

data_set = np.array(temp_data)
