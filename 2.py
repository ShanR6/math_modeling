import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину и количество кадров
frames = 200
t = np.linspace(0, 5, frames)

# Определяем функцию для системы диф. уравнений
def move_func(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = 0
    dydt = v_y
    dv_ydt = - g * m - p * m * v
    return dxdt, dv_xdt, dydt, dv_ydt
# Определяем начальные значения и параметры
g = 9.8
v = 20
m = 0.5 
p = 0.1 / 0.5

x0 = 0
v_x0 = 0
y0 = 0  
v_y0 = v

z0 = x0, v_x0, y0, v_y0
# Решаем систему диф. уравнений
def solve_func(i, key):
    sol = odeint(move_func, z0, t)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
  
  # Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
def animate(i):
    ball.set_data(solve_func(i, 'point'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=5)

edge = 30
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()
