import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10 ** 3, 10)


def radio_function(v, t):
    dNdt = F * v
    return dNdt


MM = 6 * 10 ** 10
MZ = 6 * 10 ** 24
G = 6.67 * 10 ** -11
h = 100
F = (G * MM * MZ) / (h ** 2)
v_0 = h/t

solve_Bi = odeint(radio_function, v_0, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
'''
КОПЕЦ КОНЕЧНО
'''
