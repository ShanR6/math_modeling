A = 1
while True:
  for x in range(1, 1000):
    for y in range(1, 1000):
      if not((7 * y + x < A) or (2 * x + 3 * y > 98)):
        break
    else:
      continue
    break
  else:
    print(A)
  A += 1
