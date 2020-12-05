import numpy as np
a = [1,2,3,4,5]
a1 = np.array(a)
def mul(a1):
  b = 1
  for i in range(0,len(a1)):
    A = b * a1[i]
    b = A
  print(b)
mul(a1)
