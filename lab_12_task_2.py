import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years * seconds_in_year, frames)


# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4,
     x5, v_x5, y5, v_y5) = s

    dxdt1 = v_x1
    dv_xdt1 = k * q1 * q2 * x1 / (x1 ** 2 + y1 ** 2) ** 1.5
    dydt1 = v_y1
    dv_ydt1 = k * q1 * q2 * y1 / (x1 ** 2 + y1 ** 2) ** 1.5

    dxdt2 = v_x2
    dv_xdt2 = k * q1 * q2 * x2 / (x2 ** 2 + y2 ** 2) ** 1.5
    dydt2 = v_y2
    dv_ydt2 = k * q1 * q2 * y2 / (x2 ** 2 + y2 ** 2) ** 1.5

    dxdt3 = v_x3
    dv_xdt3 = k * q1 * q2 * x3 / (x3 ** 2 + y3 ** 2) ** 1.5
    dydt3 = v_y3
    dv_ydt3 = k * q1 * q2 * y3 / (x3 ** 2 + y3 ** 2) ** 1.5

    dxdt4 = v_x4
    dv_xdt4 = k * q1 * q2 * x4 / (x4 ** 2 + y4 ** 2) ** 1.5
    dydt4 = v_y4
    dv_ydt4 = k * q1 * q2 * y4 / (x4 ** 2 + y4 ** 2) ** 1.5

    dxdt5 = v_x5
    dv_xdt5 = k * q1 * q2 * x5 / (x1 ** 2 + y1 ** 2) ** 1.5
    dydt5 = v_y5
    dv_ydt5 = k * q1 * q2 * y5 / (x1 ** 2 + y1 ** 2) ** 1.5

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4,
            dxdt5, dv_xdt5, dydt5, dv_ydt5)


# Определяем начальные значения и параметры
k = 9 * 10 ** (9)
m = 1.98 * 10 ** (30)
q1 = 1
q2 = 3

x10 = 149 * 10 ** 9
v_x10 = 0
y10 = 0
v_y10 = 30000

x20 = 0
v_x20 = -47360
y20 = 0.387 * 149 * 10 ** 9
v_y20 = 0

x30 = - 108 * 10 ** 6
v_x30 = 0
y30 = 0
v_y30 = - 35 * 10 ** 3

x40 = 0
v_x40 = -24.13 * 10 ** 3
y40 = 228 * 10 ** 6
v_y40 = 0

x50 = 0
v_x50 = -200 * 10 ** 3
y50 = 2.99196 * 10 ** 11
v_y50 = 0

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50)


# Решаем систему диф. уравнений
def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        x2 = sol[i, 4]
        y2 = sol[i, 6]
        x3 = sol[i, 8]
        y3 = sol[i, 10]
        x4 = sol[i, 12]
        y4 = sol[i, 14]
        x5 = sol[i, 16]
        y5 = sol[i, 18]
    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
        x2 = sol[:i, 4]
        y2 = sol[:i, 6]
        x3 = sol[:i, 8]
        y3 = sol[:i, 10]
        x4 = sol[:i, 12]
        y4 = sol[:i, 14]
        x5 = sol[:i, 16]
        y5 = sol[:i, 18]
    return ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))


# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color='b')

ball2, = plt.plot([], [], 'o', color='r')
ball_line2, = plt.plot([], [], '-', color='r')

ball3, = plt.plot([], [], 'o', color='g')
ball_line3, = plt.plot([], [], '-', color='g')

ball4, = plt.plot([], [], 'o', color='m')
ball_line4, = plt.plot([], [], '-', color='m')

ball5, = plt.plot([], [], 'o', color='k')
ball_line5, = plt.plot([], [], '-', color='k')

plt.plot([0], [0], 'o', color='y', ms=20)


def animate(i):
    ball1.set_data(solve_func(i, 'point')[0])

    ball2.set_data(solve_func(i, 'point')[1])

    ball3.set_data(solve_func(i, 'point')[2])

    ball4.set_data(solve_func(i, 'point')[3])

    ball5.set_data(solve_func(i, 'point')[4])

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 2 * x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()