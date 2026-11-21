#ищем все числа , которые содержат цифру 5 до тысячи
def search_by_string():
    for i in range(1,1001):
        if '5' in str(i):
            print(i)
def search_by_number():
    for i in range(1,1001):
        k=i
        while k!=0:
            if k%10==5:
                print(i)
                break
            k=k//10
