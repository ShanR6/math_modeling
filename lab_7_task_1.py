import matplotlib.pyplot as plt
import numpy as np
def ris(f,R):
  if f=='c':
    t=np.arange(-2*np.pi, 2*np.pi, 0.1)
    x=R*(t-np.sin(t)**3)
    y=R*(1-np.cos(t)**3)
  elif f=='a':
    t=np.arange(-2*np.pi, 2*np.pi, 0.1)
    R1=R/4
    x=R1*np.cos(t)**3
    y=R1*np.sin(t)**3
  plt.plot(x,y,ls='--',lw=3)
  plt.axis('equal')
  plt.show()
  return x,y

print(ris(f='a',R=5))
