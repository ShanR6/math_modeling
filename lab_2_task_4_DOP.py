a=int(input('Введите натуральное число: '))
i=2
while i<a:
  if a%i==0:
    print(i)
    a=a/i
  else:
    i=i+1
print(int(a))
