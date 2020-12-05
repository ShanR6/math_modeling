def func(a=2,b=15):
  x = int(input('Введите x:'))
  N1 = int(input('1 точка:'))
  N2 = int(input('2 точка:'))
  if a<x<b and (x==N1 or x==N2):
    y=x*x
    print(y)
func()
#----------------------------------
print('Функция y=x*x')
def func(a=2,b=15):
  N1 = int(input('1 точка:'))
  N2 = int(input('2 точка:'))
  if a<N1<b:
    y1=N1*N1
    print('В первой точке:',y1)
  if a<N2<b:
    y2=N2*N2
    print('Во второй точке:',y2)
func()
