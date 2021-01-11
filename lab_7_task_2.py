import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 
ball, = plt.plot([], [], 'o', color='r', label='Ball')
alpha=np.arange(0,2*np.pi,0.1)
xdata, ydata = [], []
def circle(R,time):
  x=R*np.cos(alpha)
  y=R*np.sin(alpha)
  return x,y
edge=3
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)

def update(frame):
  xdata.append(frame)
  ydata.append(np.sin(frame))
  def animate(i):
    ball.set_data(xdata,ydata,(circle(time=i,R=alpha*i)))
ani=FuncAnimation(fig,
update,
frames=100,
interval=30
)
ani.save('lab_7_task_2.gif')
#-----------------------------------
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 
ball, = plt.plot([], [], '-', color='r', label='Ball')
alpha=np.arange(0,2*np.pi,0.1)
R=3
xdata, ydata = [], []
t=np.arange(0,2*np.pi,0.1)
edge=10
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
R=3
def update(frame):
  R=3
  xdata.append(R*np.cos(frame))
  ydata.append(R*np.sin(frame))
  ball.set_data(xdata,ydata)
  return ball,
  
ani=FuncAnimation(fig,
update,
frames=100,
interval=30
)
ani.save('lab_7_task_2.gif')
