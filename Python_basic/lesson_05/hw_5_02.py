# Задача 2. Максимум из трёх чисел 2
# Как-то у нас уже было задание на нахождение максимума из трёх чисел с помощью дополнительной переменной.
# Теперь, когда вы знаете намного больше, вы можете оптимизировать программу, не тратя память компьютера на лишние переменные.
# Напишите программу, которая находит максимум из трёх чисел, не используя дополнительные переменные.

number_a, number_b, number_c = map(int, input('Введите через пробел три числа: ').split())
if number_a > number_b and number_a > number_c:
    print(number_a)
elif number_b > number_c and number_b > number_a:
    print(number_b)
else:
    print(number_c)