import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
def ris(f):
  if f=='b':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='Ball')

    def babochka(time):
      alpha = np.arange(0,12*np.pi,0.1)
      x = np.sin(alpha)*(np.exp(np.cos(alpha))-2*np.cos(4*alpha)+np.sin(alpha/12)**5)
      y = np.cos(alpha)*(np.exp(np.cos(alpha))-2*np.cos(4*alpha)+np.sin(alpha/12)**5)
      return x, y

    plt.axis('equal')
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)

    def animate(i):
      ball.set_data(babochka(time=i))
    ani = FuncAnimation(fig,
    animate,
    frames=100,
    interval=30
    )
    ani.save('lab_7_task_3.gif')
  elif f=='h':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='Ball')

    def heart(time):
      alpha = (0,2*np.pi,0.1)
      x = 16*np.sin(alpha)**3
      y = 13*np.cos(alpha)-5*np.cos(2*alpha)-2*np.cos(3*alpha)-np.cos(4*alpha)
      return x, y

    plt.axis('equal')
    ax.set_xlim(-20,20)
    ax.set_ylim(-20,20)

    def animate(i):
      ball.set_data(heart(time=i))
    ani = FuncAnimation(fig,
    animate,
    frames=100,
    interval=30
    )
    ani.save('lab_7_task_3.gif')
print(ris(f='b'))
