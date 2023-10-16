# - Программа принимает на вход целочисленные значения j, k, n, m
# - Программа создаёт список размерности k и заполняет его уникальными рандомными значениями в диапазоне от n до m 
# - Программа реализует поиск значения j на основе алгоритма бинарного поиска
# - Программа выводит на экран индекс искомого значения j в списке и само искомое значение j

import random

j = int(input('Введите значение j'))
k = int(input('Введите значение k'))
n = int(input('Введите значение n'))
m = int(input('Введите значение m'))

print('значение j = ', j, 'значение k = ', k, 'значение n = ', n, 'значение m = ', m)

if n >= m:
    print("Ошибка: n должно быть меньше m")
    exit()
else:
    for i in range(n, m + 1):
        print(i)

my_list = []
count = 0

while count < k:
    number = random.randrange(n, m)

    if number not in my_list:
        my_list.append(number)
        count += 1

my_list.sort()

print('Список отсортированных значений:', my_list)

mid = len(my_list) // 2
low = 0
high = len(my_list) - 1

while my_list[mid] != j and low <= high:
    if j > my_list[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("Значение j не найдено!")
else:
    print("Индекс искомого числа в списке:", mid, 'искомое число:', my_list[mid])
