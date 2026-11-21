import random
N=25
a = [random.randint(30,180) for _ in range(N)]
#первое решение
sumnechetnih = sum([x for x in a if x%2!=0])
minchetnih = min([y for y in a if y%2==0])
print('Массив 25 чисел от 30 до 180:',a)
print('Сумма нечетных:',sumnechetnih)
print('минимальный среди четных:',minchetnih)
#второе решение
minch = 1000
sum = 0
for i in a:
    if i%2!=0:
        sum += i
    if i%2==0 and i < minch:
        minch = i
print('Массив 25 чисел от 30 до 180:',a)
print('Сумма нечетных:', sum)
print('минимальный среди четных:',minch)

