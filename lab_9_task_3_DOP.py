import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 365, 0.1)


def radio_function(w, t):
  dWdt = (R**2 * L) / (a * w)
  return dWdt

w_0 = 0
w = (2 * np.pi)/365
L = 3.827 * 10 ** 26
a = 147 * 10 ** 6
v = 30.4
R = 6400
solve_Bi = odeint(radio_function, w_0, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
