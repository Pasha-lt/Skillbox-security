print('Задача 5. Число Эйлера')

# Напишите программу, которая находит сумму  ряда с точностью до 1e-5.

# P.S: Формулу смотреть на сайте :)

# Пример:

# Точность: 1e-20
# Результат: 2.7182818284590455

from math import factorial

precision = float(input('Точность: '))

i = 0
result = 0
addMember = 1

while addMember > precision:
    addMember = 1 / factorial(i)
    i += 1
    result += addMember

print(f'Результат: {result}')
