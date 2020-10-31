a = int(input('Введите число: '))
for i in range(0,a):
    s=1
    for j in range(2,i//2+1):
        if i%j==0:
            s+=j
    if s==i:
        print(i)