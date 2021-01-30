import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='b')
ball1, = plt.plot([], [], '-', color='b')
ball2, = plt.plot([], [], '-', color='b')
ball3, = plt.plot([], [], '-', color='b')
ball4, = plt.plot([], [], '-', color='b')
ball5, = plt.plot([], [], '-', color='b')
ball6, = plt.plot([], [], '-', color='b')
ball7, = plt.plot([], [], '-', color='b')
ball8, = plt.plot([], [], '-', color='b')


def circle_move(phi, time, t):
    vy0 = 0.02 * t
    a = 0.001 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi)
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move1(phi, time, t):
    vy0 = 0.02 * t
    a = 0.001 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 30
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move2(phi, time, t):
    vy0 = 0.023 * t
    a = 0.0016 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 60
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move3(phi, time, t):
    vy0 = 0.029 * t
    a = 0.0018 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 30
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move4(phi, time, t):
    vy0 = 0.022 * t
    a = 0.0014 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 60
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move5(phi, time, t):
    vy0 = 0.026 * t
    a = 0.0011 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 50
    y = y0 + R * np.sin(phi) + 40
    return x, y


def circle_move6(phi, time, t):
    vy0 = 0.0234 * t
    a = 0.00112 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 20
    y = y0 + R * np.sin(phi) + 35
    return x, y


def circle_move7(phi, time, t):
    vy0 = 0.0272 * t
    a = 0.00193 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 10
    y = y0 + R * np.sin(phi) + 50
    return x, y


def circle_move8(phi, time, t):
    vy0 = 0.0272 * t
    a = 0.00194 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 45
    y = y0 + R * np.sin(phi) + 20
    return x, y


edge = 140
plt.axis('equal')
ax.set_xlim(-80, 80)
ax.set_ylim(0, edge)


def animate(i):
    ball.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball1.set_data(circle_move1(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball2.set_data(circle_move2(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball3.set_data(circle_move3(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball4.set_data(circle_move4(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball5.set_data(circle_move5(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball6.set_data(circle_move6(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball7.set_data(circle_move7(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball8.set_data(circle_move8(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))


ani = FuncAnimation(fig,
                    animate,
                    frames=100,
                    interval=30
                    )
ani.save('kipenie.gif')
