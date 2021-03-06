import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(1, 1000, 10)


def radio_function(v, t):
  dvdt = a_0 - (y * v**2)/m
  return dvdt
y = 0.5
m = 70
a_0 = 3
v_0 = 0

solve_Bi = odeint(radio_function, v_0, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
