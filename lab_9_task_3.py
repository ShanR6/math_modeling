import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 100, 1)


def radio_function(v, t):
    dNdt = F / (v ** 2) * y
    return dNdt


y = 0.5
m = 70
F = 100
a0 = F / m
v_0 = 1 + a0

solve_Bi = odeint(radio_function, v_0, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
