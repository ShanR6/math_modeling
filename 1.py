import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину

seconds_in_day = 24 * 60 * 60
seconds_in_year = 365 * 24 * 60 * 60
years = 2
t = np.arange(0, years*seconds_in_year, seconds_in_day)

# Определяем функцию для системы диф. уравнений

def move_func(s, t):
  (x1, v_x1, y1, v_y1,
   x2, v_x2, y2, v_y2,
   x3, v_x3, y3, v_y3) = s

# Диманика первого тела под влиянием второго и третьего

dxdt1 = v_x1
dv_xdt1 = (- G * m2 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5 - G * m3 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5 + k * q1 * q2 / m1 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5 + k * q1 * q3 / m1 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)

dy_dt1 = v_y1
dv_ydt1 = (- G * m2 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5 - G * m3 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5 + k * q1 * q2 / m1 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5 + k * q1 * q3 / m1 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)

dxdt2 = v_x2
dv_xdt2 = (- G * m1 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5 - G * m3 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5 + k * q2 * q1 / m2 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5 + k * q2 * q3 / m2 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)

dy_dt2 = v_y2
dv_ydt2 = (- G * m1 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5 - G * m3 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5 + k * q2 * q1 / m2 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5 + k * q2 * q3 / m2 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)

dxdt3 = v_x3
dv_xdt3 = (- G * m1 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5 - G * m2 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5 + k * q3 * q1 / m3 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5 + k * q3 * q2 / m3 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)

dy_dt3 = v_y3
dv_ydt3 = (- G * m1 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5 - G * m2 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5 + k * q3 * q1 / m3 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5 + k * q3 * q2 / m3 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)

