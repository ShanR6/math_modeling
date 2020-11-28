import numpy as np
M = 4
N = 3
a = np.ndarray(shape=(N,M))
b = np.ndarray(shape=(N,M))
c = np.ndarray(shape=(N,M))
for i in range(N):
  for j in range(M):
    z0 = int(float(input('Первый массив - ')))
    z1 = np.array(z0)
    a = z1
for i in range(N):
  for j in range(M):
    z2 = int(float(input('Второй массив - ')))
    z3 = np.array(z2)
    b = z3
for i in range(N):
  for j in range(M):
    if a[i][j] > b[i][j]:
      c[i][j] = a[i][j]
    else:
      c[i][j] = b[i][j]
print(a)
print(b)
print(c)
