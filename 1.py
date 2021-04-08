def dell(n, m):
  return n % m == 0

A = 1
while True:
  found = False
  for x in range(1, 10**6):
    if not (dell(130, A) and (((not dell(x, A)) and dell(x, 38)) <= (not dell(x, 78)))):
      found = True
      break
  if not found:
    print(A)
  A += 1
  
