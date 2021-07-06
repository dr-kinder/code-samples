# regression.py
# -------------------------------------------------------------------------
# Example of linear regression on data from first passage problem.
# first_passage.py must be in the working directory.
# This could take a while to finish if (samples x nmax) ~ 10**8 or more.
# ------------------------------------------------------------------------- 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

from first_passage import first_passage

#%% Define and run simulations.
data = {}		# empty dictionary to store all data
nmax = 10**6
parameters = dict(N=nmax, p=0.5)  # common inputs
l_values = [10, 20, 50, 100, 200, 500]
samples = 10**4

for l in l_values:
	data["L={}".format(l)] = \
		[first_passage(L=l, **parameters) for n in range(samples)]
step_data = pd.DataFrame(data)

#%% Prepare data for modeling with sklearn.
model = LinearRegression()

X = np.array(l_values).reshape(-1,1)
Y = step_data.mean()
logX = np.log(X)
logY = np.log(Y)
xFit = np.linspace(1, X.max(), 201).reshape(-1,1)

#%% Plot data and fit models.
plt.figure()
plt.plot(X, Y, 'ko', mew=2, mfc='none', label="Data")

# Check for linear relationship.
model.fit(X, Y)
print("Linear Model: A + b*x")
print("A = {:.3f}, b = {:.3f}".format(model.intercept_, model.coef_[0]))
print("R2: ", model.score(X,Y))
yFit = model.predict(xFit)
plt.plot(xFit, yFit, 'r-', label="Linear Model")

# Check for exponential relationship.
model.fit(X, logY)
print("Exponential Model: A * exp(b*x)")
print("A = {:.3f}, b = {:.3f}".format(model.intercept_, model.coef_[0]))
print("R2: ", model.score(X,Y))
yFit = model.predict(xFit)
plt.plot(xFit, np.exp(yFit), 'g-', label="Exponential Model")

# Check for power-law relationship.
model.fit(logX, logY)
print("Power Law Model: A * x**b")
print("A = {:.3f}, b = {:.3f}".format(model.intercept_, model.coef_[0]))
print("R2: ", model.score(X,Y))
yFit = model.predict(np.log(xFit))
plt.plot(xFit, np.exp(yFit), 'b-', label="Power Law Model")

plt.legend()
plt.show
