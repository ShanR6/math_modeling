import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.1)


def diff_func(q, t):
    x, y, z, w = q
    dx_dy_dz = w
    w_dt = -2 * x - y + 4 * z
    return dx_dy_dz, w_dt


x0 = -71
y0 = 1
z0 = -3
w0 = x0 - y0 - z0
q0 = x0, y0, z0, w0

sol = odeint(diff_func, q0, t)

plt.plot(t, sol[:, 0], 'b')
plt.plot(t, sol[:, 1], 'r')
plt.show()
