# ivp_comparison.py
# -------------------------------------------------------------------------
# Compare different ODE solvers using solve_ivp.
# ------------------------------------------------------------------------- 
import numpy as np, matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define ODE to integrate: simple harmonic oscillator.
def f(t,y): return [ y[1], -y[0] ]

# Define time interval.
t_min = 0
t_max = 10

# Define initial conditions.
y0 = [1.0, 0.0]

# Integrate the ODE using defaults.
result = solve_ivp(f, (t_min, t_max), y0)
plt.plot(result.t, result.y[0], '^k', label='RK45')

# Specify time series and use different solver.
dt = 0.1
t_vals = np.arange(t_min, t_max + dt, dt)

result = solve_ivp(f, (t_min, t_max), y0, t_eval=t_vals, method='BDF')
plt.plot(result.t, result.y[0], '.r', label='BDF')

plt.legend()
plt.show()
