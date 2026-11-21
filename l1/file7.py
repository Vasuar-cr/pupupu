import random
m = int(input('Введите число:'))
a = [random.randint(-100,100) for _ in range(m)]
#первое решение
set_a = set(a)
print('массив m чисел:',a)
print('Количество уникальных чисел:', len(set_a))
#второе решение
unique_elements = []
for x in a:
    if x not in unique_elements:
        unique_elements.append(x)
cnt = len(unique_elements)
print('Количество уникальных чисел:', cnt)