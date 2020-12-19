import matplotlib.pyplot as plt
import numpy as np
from math import pi,sin
def lissaju(A=1,a=1,B=5,b=0.5,t=4):
  f=pi/2
  x=A*sin(a*t+f)
  y=B*sin(b*t)
  X,Y=np.meshgrid(x,y)
  fxy= 
  plt.contour(X,Y,fxy,[2])
  plt.show()
lissaju()
