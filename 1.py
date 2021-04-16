f = 0
count = 0
for x in range(2320, 10988):
  if (x % 2 == 0 or x % 7 == 0) and x % 11 != 0 and x % 13 != 0 and x % 17 != 0 and x % 19 != 0:
    f = x
    count += 1
print(count, f)
