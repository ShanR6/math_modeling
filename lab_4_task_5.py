from math import pi,sqrt
y=input('Выберете фигуру: круг(k), прямоугольник(p), треугольник(t):')
if y == 'k':
  R=int(input('Введите радиус круга:'))
  def kr(R):
    if R>=0:
      S1 = pi*R**2
      print(S1)
  kr(R)
elif y == 'p':
  a1 = int(input('Введите первую сторону:'))
  a2 = int(input('Введите вторую сторону:'))
  def pr(a1,a2):
    if a1>0 and a2>0:
      S2 = a1*a2
      print(S2)
  pr(a1,a2)
elif y == 't':
  a = int(input('Введите первую сторону:'))
  b = int(input('Введите вторую сторону:'))
  c = int(input('Введите третью сторону:'))
  def tr(a,b,c):
    if a>0 and b>0 and c>0 and a!=b+c and a<b+c and b!=a+c and b<a+c and c!=a+b and c<a+b:
      z = (a+b+c)/2
      S = sqrt(z*(z-a)*(z-b)*(z-c))
      print(S)
  tr(a,b,c)