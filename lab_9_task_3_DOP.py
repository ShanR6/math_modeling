import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 24, 1)


def radio_function(S, t):
    dvdt = R * ((S * np.cos(ugol)) * gg)
    return dvdt


L = 3.827 * 10 ** 26
q = 147 * 10 ** 6
v = 30.4
R = 6400
solve_Bi = odeint(radio_function, S_0, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
