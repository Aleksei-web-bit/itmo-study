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
else:
    for i in range(n, m + 1):
        print(i)

my_list = []
count = 0

while count < k:
    numbers = random.randrange(n, m)

    if numbers not in my_list:
        my_list.append(numbers)
        count += 1
    else:
        format(numbers)

my_list.sort()

print(my_list)
