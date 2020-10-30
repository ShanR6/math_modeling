n = int(input('Введите число элементов ряда Фибоначчи:'))
a=b=1
if n==1:
  print(a)
elif n<1:
  print('-')
else:
  print(a,end=' ')
  print(b,end=' ')
for i in range(2,n):
  a,b=b,a+b
  print(b,end=' ')  