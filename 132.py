import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='b')

def circle_move(R, vx0, vy0, time):
  x0 = vx0 * time
  y0 = vy0 * time
  alpha = np.arange(0, 2*np.pi, 0.1)
  x = x0 + R*np.cos(alpha)
  y = y0 + R*np.sin(alpha)
  return x, y

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
  ball.set_data(circle_move(R=2, vx0=0, vy0=1, time=i))
ani = FuncAnimation(fig,
animate,
frames=100,
interval=30
)
ani.save('kipenie.gif')
