N = 5
a=[]
for i in range(N):
  num = int(input())
  a.(num)
print(a)
num = int(input("Число: "))
j = int(input("Позиция: "))
a.append(num)
while N > j-1:
    a[N], a[N-1] = a[N-1], a[N]
    N -= 1
print(a)
