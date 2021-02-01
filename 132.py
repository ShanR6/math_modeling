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
ball21, = plt.plot([], [], '-', color='b')
ball22, = plt.plot([], [], '-', color='b')
ball23, = plt.plot([], [], '-', color='b')
ball24, = plt.plot([], [], '-', color='b')
ball25, = plt.plot([], [], '-', color='b')
ball26, = plt.plot([], [], '-', color='b')
ball27, = plt.plot([], [], '-', color='b')
ball28, = plt.plot([], [], '-', color='b')
ball29, = plt.plot([], [], '-', color='b')
ball30, = plt.plot([], [], '-', color='b')


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
        a = 0.000018 * 70 * t
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
        a = 0.000014 * 70 * t
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
        a = 0.000011 * 70 * t
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
        a = 0.0000112 * 70 * t
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
        a = 0.0000193 * 70 * t
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
        a = 0.0000194 * 70 * t
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
        a = 0.00001964 * 70 * t
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
        a = 0.0000195744 * 70 * t
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
        a = 0.0000192454 * 70 * t
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
        a = 0.000019744 * 70 * t
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
        a = 0.0000193674 * 70 * t
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
        a = 0.000019446424 * 70 * t
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
        a = 0.00001937634 * 70 * t
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
        a = 0.0000193674 * 70 * t
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
        a = 0.000019284 * 70 * t
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
        a = 0.0000190384 * 70 * t
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
        a = 0.0000199254 * 70 * t
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
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 55
    y = y0 + R * np.sin(phi) - 40
    return x, y


def circle_move21(phi, time, t):
    if t >= 90:
        a = 0.000019272169324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 45
    y = y0 + R * np.sin(phi) - 40
    return x, y


def circle_move22(phi, time, t):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 13
    y = y0 + R * np.sin(phi) - 50
    return x, y


def circle_move23(phi, time, t):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 16
    y = y0 + R * np.sin(phi) - 55
    return x, y


def circle_move24(phi, time, t):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 16
    y = y0 + R * np.sin(phi) - 35
    return x, y


def circle_move25(phi, time, t):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 25
    y = y0 + R * np.sin(phi) - 45
    return x, y


def circle_move26(phi, time, t):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 8
    y = y0 + R * np.sin(phi) - 34
    return x, y


def circle_move27(phi, time, t):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 17
    y = y0 + R * np.sin(phi) - 52
    return x, y


def circle_move28(phi, time, t):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) + 50
    y = y0 + R * np.sin(phi) - 25
    return x, y


def circle_move29(phi, time, t):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 23
    y = y0 + R * np.sin(phi) - 46
    return x, y


def circle_move30(phi, time, t):
    if t >= 90:
        a = 0.000019279324 * 70 * t
    else:
        a = 0.000019279324 * t
    vy0 = 0.0272157 * t
    y0 = vy0 * time
    alpha = a * (np.pi / 180) * time
    R = alpha * time
    x = R * np.cos(phi) - 23
    y = y0 + R * np.sin(phi) - 55
    return x, y


edge = 200
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(0, edge)


def animate(i):
    ball.set_data(circle_move(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball1.set_data(circle_move1(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball2.set_data(circle_move2(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball3.set_data(circle_move3(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball4.set_data(circle_move4(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball5.set_data(circle_move5(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball6.set_data(circle_move6(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball7.set_data(circle_move7(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball8.set_data(circle_move8(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball9.set_data(circle_move9(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball10.set_data(circle_move10(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball11.set_data(circle_move11(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball12.set_data(circle_move12(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball13.set_data(circle_move13(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball14.set_data(circle_move14(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball15.set_data(circle_move15(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball16.set_data(circle_move16(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball17.set_data(circle_move17(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball18.set_data(circle_move18(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball19.set_data(circle_move19(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball20.set_data(circle_move20(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball21.set_data(circle_move21(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball22.set_data(circle_move22(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball23.set_data(circle_move23(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball24.set_data(circle_move24(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball25.set_data(circle_move25(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball26.set_data(circle_move26(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball27.set_data(circle_move27(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball28.set_data(circle_move28(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball29.set_data(circle_move29(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))
    ball30.set_data(circle_move30(phi=np.linspace(0, 2 * np.pi, 50), time=i, t=70))


ani = FuncAnimation(fig,
                    animate,
                    frames=200,
                    interval=30
                    )
ani.save('kipenie.gif')
