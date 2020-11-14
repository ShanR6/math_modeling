from lab_3_task_1 import g
import numpy as np
x0 = 2
y0 = 3
V0 = 4
t = range(0,6)
T = np.array(t)
x = x0 + V0*T
y = y0 + V0*T - (g*(T**2))/2
print('t -',t)
print('x -',x)
print('y -',y)