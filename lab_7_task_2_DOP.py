import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()
move,=plt.plot([],[],'o',color='r',label='Frak')

def sin_move(vx0,vy0,A,f,t,time):
  time=np.arange(0,10,0.1)
  y0=vy0*time
  x=np.arange(0,10,0.1)
  y=y0+A*np.sin(f*t)
  return x,y
plt.axis('equal')
ax.set_xlim(-3,3)
ax.set_ylim(-3,3)

def animate(i):
  move.set_data(sin_move(vx0=0.01,vy0=0.01,time=i,A=30,f=10,t=20))
ani=FuncAnimation(fig,
animate,
frames=100,
interval=30
)
ani.save('lab_7_task_2_DOP.gif')
