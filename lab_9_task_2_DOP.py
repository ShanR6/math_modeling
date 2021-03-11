import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,24,1)


def radio_function(S, t):
  dvdt = R/S
  return dvdt
if t==0:
  S_0 = 1600 * 10**-4
elif t == 12:
  S_0 = 2500 * 10**-4
if t == 18:
  cos = 90
S=2*np.pi**2
R = np.sqrt(S)/np.pi
gg = 1370
solve_Bi = odeint(radio_function, S_0, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
