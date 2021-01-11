import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()
move,=plt.plot([],[],'o',color='r',label='Frak')

def first(R,time):
  t=np.arange(-2*np.pi,2*np.pi,0.1)
  x=R*(t-np.sin(t)**3)
  y=R*(1-np.cos(t)**3)
  return x,y
def second(R,time):
  t=np.arange(-2*np.pi,2*np.pi,0.1)
  x=(R/4)*np.cos(t)**3
  y=(R/4)*np.sin(t)**3
  return x,y
plt.axis('equal')
ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
def animate(i):
  move.set_data(first(time=i,R=5),second(time=i,R=5))
ani=FuncAnimation(fig,
animate,
frames=100,
interval=30
)
ani.save('lab_7_task_1_DOP.gif')
