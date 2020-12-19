import matplotlib.pyplot as plt
import numpy as np
from math import sqrt,pi,sin
def ris(e=1,b=3,f=4,k=5):
  r0=e**(b*f)
  r1=k*f
  r2=k/sqrt(f)
  r3=sin(k*f)