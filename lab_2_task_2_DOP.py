a=int(input('Введите длину первого отрезка: '))
b=int(input('Введите длину второго отрезка: '))
c=int(input('Введите длину третьего отрезка: '))
if a>=b+c or b>=a+c or c>=a+b:
  print('Такой треугольник не существует') 
elif a==b==c:
  print('Треугольник - равносторонний')
elif (a==b and b!=c) or (a==c and a!=b) or (b==c and c!=a):
  print('Треугольник - равнобедренный')
elif a!=b!=c:
  print('Треугольник - разносторонний')