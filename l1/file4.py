import random
N=int(input('ВВЕДИТЕ ЧИСЛО:'))
a = [random.randint(-100,100) for _ in range(N)]
cnt = 0
for i in a:
    if i>0:
        cnt+=1
print(a)
print('Количество положительных чисел:',cnt)
