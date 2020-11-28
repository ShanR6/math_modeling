x0 = 10 # Глобальная переменная
def move(t):
  x = x0*t # Локальная переменная
  return x
print(move(3))
# print(x)
x = 'Good'
def my_func():
  x = 'Bad'
  print(x)
my_func()
print(x)