import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)


def diff_func(z, x):
    w, t = z

    dy_dt = w
    dw_dt = np.sin(x) + np.cos(x)

    return dy_dt, dw_dt


t0 = 1
w0 = 3/t0
z0 = w0, t0

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 0], 'b')
plt.plot(x, sol[:, 1], 'r')

plt.show()
