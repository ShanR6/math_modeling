import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)


def diff_func(z, x):
    w, y = z
    dy_dx = w
    dw_dx = (w - ((3*y**2)/np.sqrt(x)))/y
    return dy_dx, dw_dx


y0 = 0
w0 = 1
z0 = w0, y0
sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 0], 'b')
plt.plot(x, sol[:, 1], 'r')
plt.show()
