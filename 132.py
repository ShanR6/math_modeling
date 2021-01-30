import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='b')
ball1, = plt.plot([], [], '-', color='b')
ball2, = plt.plot([], [], '-', color='b')
ball3, = plt.plot([], [], '-', color='b')
ball4, = plt.plot([], [], '-', color='b')


def circle_move(phi, a, time, vx0, vy0):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = x0 + R * np.cos(phi)
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move1(phi, a, time, vx0, vy0):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = x0 + R * np.cos(phi) + 15
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move2(phi, a, time, vx0, vy0):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = x0 + R * np.cos(phi) + 30
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move3(phi, a, time, vx0, vy0):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = x0 + R * np.cos(phi) - 15
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move4(phi, a, time, vx0, vy0):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = x0 + R * np.cos(phi) - 30
    y = y0 + R * np.sin(phi)
    return x, y


edge = 50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(0, edge)


def animate(i):
    ball.set_data(circle_move(a=0.025, phi=np.linspace(0, 2 * np.pi, 50), vx0=0, vy0=0.5, time=i))
    ball1.set_data(circle_move1(a=0.025, phi=np.linspace(0, 2 * np.pi, 50), vx0=0, vy0=0.5, time=i))
    ball2.set_data(circle_move2(a=0.025, phi=np.linspace(0, 2 * np.pi, 50), vx0=0, vy0=0.5, time=i))
    ball3.set_data(circle_move3(a=0.025, phi=np.linspace(0, 2 * np.pi, 50), vx0=0, vy0=0.5, time=i))
    ball4.set_data(circle_move4(a=0.025, phi=np.linspace(0, 2 * np.pi, 50), vx0=0, vy0=0.5, time=i))


ani = FuncAnimation(fig,
                    animate,
                    frames=100,
                    interval=30
                    )
ani.save('kipenie.gif')
