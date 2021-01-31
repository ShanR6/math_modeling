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
ball9, = plt.plot([], [], '-', color='b')
ball10, = plt.plot([], [], '-', color='b')
ball11, = plt.plot([], [], '-', color='b')
ball12, = plt.plot([], [], '-', color='b')
ball13, = plt.plot([], [], '-', color='b')
ball14, = plt.plot([], [], '-', color='b')
ball15, = plt.plot([], [], '-', color='b')
ball16, = plt.plot([], [], '-', color='b')
ball17, = plt.plot([], [], '-', color='b')
ball18, = plt.plot([], [], '-', color='b')
ball19, = plt.plot([], [], '-', color='b')
ball20, = plt.plot([], [], '-', color='b')


def circle_move(phi, time, t):
    if t >= 90:
        a = 0.00001 * 70 * t
    else:
        a = 0.00001 * t
    vy0 = 0.02 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi)
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move1(phi, time, t):
    if t >= 90:
        a = 0.00001 * 70 * t
    else:
        a = 0.00001 * t
    vy0 = 0.02 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 30
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move2(phi, time, t):
    if t >= 90:
        a = 0.000016 * 70 * t
    else:
        a = 0.000016 * t
    vy0 = 0.023 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 60
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move3(phi, time, t):
    if t >= 90:
        a = 0.000018 * 50 * t
    else:
        a = 0.000018 * t
    vy0 = 0.029 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 30
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move4(phi, time, t):
    if t >= 90:
        a = 0.000014 * 50 * t
    else:
        a = 0.000014 * t
    vy0 = 0.022 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 60
    y = y0 + R * np.sin(phi)
    return x, y


def circle_move5(phi, time, t):
    if t >= 90:
        a = 0.000011 * 50 * t
    else:
        a = 0.000011 * t
    vy0 = 0.026 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 50
    y = y0 + R * np.sin(phi) + 40
    return x, y


def circle_move6(phi, time, t):
    if t >= 90:
        a = 0.0000112 * 50 * t
    else:
        a = 0.0000112 * t
    vy0 = 0.0234 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 20
    y = y0 + R * np.sin(phi) + 35
    return x, y


def circle_move7(phi, time, t):
    if t >= 90:
        a = 0.0000193 * 50 * t
    else:
        a = 0.0000193 * t
    vy0 = 0.0272 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 10
    y = y0 + R * np.sin(phi) + 50
    return x, y


def circle_move8(phi, time, t):
    if t >= 90:
        a = 0.0000194 * 50 * t
    else:
        a = 0.0000194 * t
    vy0 = 0.0272 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 45
    y = y0 + R * np.sin(phi) + 20
    return x, y


def circle_move9(phi, time, t):
    if t >= 90:
        a = 0.00001964 * 50 * t
    else:
        a = 0.00001964 * t
    vy0 = 0.02722 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 50
    y = y0 + R * np.sin(phi) + 5
    return x, y


def circle_move10(phi, time, t):
    if t >= 90:
        a = 0.0000195744 * 50 * t
    else:
        a = 0.0000195744 * t
    vy0 = 0.02672 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 55
    y = y0 + R * np.sin(phi) + 35
    return x, y


def circle_move11(phi, time, t):
    if t >= 90:
        a = 0.0000192454 * 50 * t
    else:
        a = 0.0000192454 * t
    vy0 = 0.0276262 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 3
    y = y0 + R * np.sin(phi) - 10
    return x, y


def circle_move12(phi, time, t):
    if t >= 90:
        a = 0.000019744 * 50 * t
    else:
        a = 0.000019744 * t
    vy0 = 0.0272 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 20
    y = y0 + R * np.sin(phi) - 20
    return x, y


def circle_move13(phi, time, t):
    if t >= 90:
        a = 0.0000193674 * 50 * t
    else:
        a = 0.0000193674 * t
    vy0 = 0.0274672 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 45
    y = y0 + R * np.sin(phi) - 13
    return x, y


def circle_move14(phi, time, t):
    if t >= 90:
        a = 0.000019446424 * 50 * t
    else:
        a = 0.000019446424 * t
    vy0 = 0.02724235 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 35
    y = y0 + R * np.sin(phi) - 30
    return x, y


def circle_move15(phi, time, t):
    if t >= 90:
        a = 0.00001937634 * 50 * t
    else:
        a = 0.00001937634 * t
    vy0 = 0.0273672 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 50
    y = y0 + R * np.sin(phi) - 3
    return x, y


def circle_move16(phi, time, t):
    if t >= 90:
        a = 0.0000193674 * 50 * t
    else:
        a = 0.0000193674 * t
    vy0 = 0.02757632 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 6
    y = y0 + R * np.sin(phi) - 12
    return x, y


def circle_move17(phi, time, t):
    if t >= 90:
        a = 0.000019284 * 50 * t
    else:
        a = 0.000019284 * t
    vy0 = 0.0273732 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 55
    y = y0 + R * np.sin(phi) - 4
    return x, y


def circle_move18(phi, time, t):
    if t >= 90:
        a = 0.0000190384 * 50 * t
    else:
        a = 0.0000190384 * t
    vy0 = 0.0279452 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 11
    y = y0 + R * np.sin(phi) - 30
    return x, y


def circle_move19(phi, time, t):
    if t >= 90:
        a = 0.0000199254 * 50 * t
    else:
        a = 0.0000199254 * t
    vy0 = 0.0282572 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 40
    y = y0 + R * np.sin(phi) - 1
    return x, y


def circle_move20(phi, time, t):
    if t >= 90:
        a = 0.000019279324 * 50 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 55
    y = y0 + R * np.sin(phi) - 20
    return x, y


edge = 200
plt.axis('equal')
ax.set_xlim(-edge, edge)
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
    ball9.set_data(circle_move9(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball10.set_data(circle_move10(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball11.set_data(circle_move11(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball12.set_data(circle_move12(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball13.set_data(circle_move13(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball14.set_data(circle_move14(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball15.set_data(circle_move15(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball16.set_data(circle_move16(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball17.set_data(circle_move17(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball18.set_data(circle_move18(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball19.set_data(circle_move19(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))
    ball20.set_data(circle_move20(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=100))


ani = FuncAnimation(fig,
                    animate,
                    frames=200,
                    interval=30
                    )
ani.save('kipenie.gif')
