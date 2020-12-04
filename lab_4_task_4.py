def func(a=2,b=15):
  x = int(input('Введите x:'))
  N1 = int(input('1 точка:'))
  N2 = int(input('2 точка:'))
  if a<x<b and (x==N1 or x==N2):
    y=x*x
    print(y)
func()