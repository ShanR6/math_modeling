print('a*x**2+b*x+c=0:')
a=float(input('Введите первый коэффициент:'))
b=float(input('Введите второй коэффициент:'))
c=float(input('Введите свободный член:'))
D=b**2-4*a*c
x1=(-b+D**0.5)/(2*a)
x2=(-b-D**0.5)/(2*a)
if D<0:
  print('Нет корней')
elif D==0:
  print(x1)
else:
  print(x1,x2)


