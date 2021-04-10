import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(0, 6, 0.01)


def diff_func(z, t):
    x, y = z
    dxdt = k1 * (A - x - y)
    dydt = k2 * (A - x - y)
    return dxdt, dydt

k1 = 0.2
k2 = 0.4
A = 200
x0 = 2
y0 = 2

z0 = x0, y0

sol = odeint(diff_func, z0, t)


plt.plot(t, sol[:,1], 'b')
plt.plot(t, sol[:,0], 'r')

plt.show()
