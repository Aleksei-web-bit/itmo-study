# Ввод значения N с клавиатуры
N = int(input("Введите целое число N: "))

# Проверка знака числа и вывод соответствующего сообщения
if N < 0:
    print("Число не равно и меньше 0")
elif N > 0:
    print("Число не равно и больше 0")
else:
    print("Число не имеет знака")
