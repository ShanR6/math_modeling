import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 1000, 10)


def radio_function(v, t):
    F = b - k * v
    dNdt = F / m
    return dNdt


b = 1
k = 2
m = 138
v_0 = 30 * t
solve_Bi = odeint(radio_function, v_0, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
