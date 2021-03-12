import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 24, 1)


def radio_function(S, t):
    dvdt = R * ((S * np.cos(ugol)) * gg)
    return dvdt


S_0 = 0
if np.any(t == 0):
    S_0 = 1600 * 10 ** -4
elif np.any(t == 12):
    S_0 = 2500 * 10 ** -4
if np.any(t == 18) or np.any(t == 6):
    ugol = 90
elif np.any(0 <= t <= 12):
    ugol = 0
R = 5
S = np.pi * R ** 2
gg = 1370
solve_Bi = odeint(radio_function, S_0, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
