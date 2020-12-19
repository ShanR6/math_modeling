import matplotlib.pyplot as plt
import numpy as np
f = input('Окружность(o) или эллипс(e):')


def ris(f,rad=50,xa=-100,xb=100,N=5):
  x = np.arange(xa,xb,N)
  y = np.arange(xa,xb,N)
  X, Y = np.meshgrid(x,y)
  if f == 'o':
    fxy = X**2 + Y**2
    plt.title('Окружность')
  elif f == 'e':
    X = 
    plt.title('Эллипс')
  
  plt.contour(X,Y,fxy,levels=[rad**2])
  plt.axis('equal')
  plt.show()
ris(f)