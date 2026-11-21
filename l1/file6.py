import random
N = 45
a = [random.uniform(100,1005) for _ in range(N)]
maxa = max(a)
ind_maxa = a.index(maxa)
print('45 вещественных чисел:',a)
print('Максимальное число:',maxa,' индекс:',ind_maxa)
print('Разность между максимумом и его индексом: ',maxa - ind_maxa)