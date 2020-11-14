from lab_3_task_1 import g, h, e, k
from math import sin, tan, cos, pi, sqrt
h = 100
a = pi/3
B = 30
V = sqrt((g*h*(tan(B)**2))/(2*(cos(a)**2)*(1-tan(B)*tan(a))))
print(V)
T = 200
E = 300
N = (2/sqrt(pi))*(h/((k*T)**(3/2)))*(e**(-E/(k*T)))*(E**(T/2))
print(N)