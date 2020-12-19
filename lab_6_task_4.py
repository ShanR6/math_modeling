import matplotlib.pyplot as plt
import numpy as np
from math import sqrt,pi,sin
w='логарифмическая спираль(l),архимедова спираль(ar), спираль жезл(j), роза(r)'
def ris(w,e=1,b=3,f=4,k=5):
  if w=='l':
    x=np.arange(0,8*pi,0.01)
    y=np.arange(0,8*pi,0.01)
    X, Y = np.meshgrid(x, y)
    r=e**(b*f)
  elif w=='ar':
    x=np.arange(0,8*pi,0.01)
    y=np.arange(0,8*pi,0.01)
    X, Y = np.meshgrid(x, y)
    r=k*f
  elif w=='j':
    x=np.arange(0.01,8*pi,0.01)
    y=np.arange(0.01,8*pi,0.01)
    X, Y = np.meshgrid(x, y)
    r=k/sqrt(f)
  elif w=='r':
    x=np.arange(0,8*pi,0.01)
    y=np.arange(0,8*pi,0.01)
    X, Y = np.meshgrid(x, y)
    r=sin(k*f)
  plt.contour(X,Y,r,levels=[0])
  plt.show()
ris(w='l')
