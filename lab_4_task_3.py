def high(m=10,v=5,h=3,g=9.81):
  E1 = (m*v**2)/2
  E2 = m*g*h
  E = E1 + E2
  print(E)
high()
#------------------------------
m = int(input('Введите массу тела:'))
v = int(input('Введите скорость тела:'))
h = int(input('Введите высоту полёта тела:'))
g = 9.81
def high(m,v,h,g):
  E1 = (m*v**2)/2
  E2 = m*g*h
  E = E1 + E2
  print(E)
high(m,v,h,g)
