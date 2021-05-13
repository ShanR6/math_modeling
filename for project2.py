import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def circle_func(x_centre_point, # х-координата центральной точки окружности
                y_centre_point, # у-координата центральной точки окружности
                R):
    """ Функция, возвращающая точки окружности относительно определенного центра
    """
    x = np.zeros(30) #Создание массива для координаты х
    y = np.zeros(30) #Создание массива для координаты у
    for i in range(0, 30, 1): # Цикл, определяющий множество точек окружности относительно центра
        alpha = np.linspace(0, 2*np.pi, 30)
        x[i] = x_centre_point + R*np.cos(alpha[i])
        y[i] = y_centre_point + R*np.sin(alpha[i])

    return x, y

# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    x, y, v_x, v_y = s

    dxdt = v_x
    dv_xdt = 0
    dydt = v_y
    dv_ydt = 0

    return dxdt, dydt, dv_xdt, dv_ydt

# Определяем начальные значения и параметры, входящие в систему диф. уравнений
N = 2000
T = 30
radius = 1

x0 = 2.5
v_x0 = 1
y0 = 4
v_y0 = 6.3
s0 = x0, y0, v_x0, v_y0

X = []
Y = []
X1 = 0
X2 = 5
Y1 = 0
Y2 = 5

tau = np.linspace(0, T, N)

for i in range(N-1):
    t=[tau[i], tau[i+1]]
    sol = odeint(move_func, s0, t)
    X.append(sol[1, 0])
    Y.append(sol[1, 1])
    x0 = sol[1, 0]
    y0 = sol[1, 1]
    vx0 = sol[1, 2]
    vy0 = sol[1, 3]
    if np.abs(x0-X1) <= radius or np.abs(x0-X2) <= radius:
        vx0 = -vx0
    if np.abs(y0-Y1) <= radius or np.abs(y0-Y2) <= radius:
        vy0 = -vy0
    s0 = x0, y0, vx0, vy0


# Построение фигуры
fig, ax = plt.subplots()
plt.xlim([X1, X2])
plt.ylim([Y1, Y2])
plt.plot([X1, Y1],[X2, Y1],color='b')
plt.plot([X2, Y1],[X2, Y2],color='b')
plt.plot([X2, Y2],[X1, Y2],color='b')
plt.plot([X1, Y2],[X1, Y1],color='b')
ball1, = plt.plot([], [], 'o', color='r', ms=1)

def animate(i):
    ball1.set_data(circle_func(X[i], Y[i], radius))

ani = FuncAnimation(fig, animate, frames=N, interval=1)

plt.axis('equal')
plt.grid()

plt.show()
