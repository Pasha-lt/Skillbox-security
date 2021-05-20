# Задача 10. Максимальное число (по желанию)
# Пользователь вводит три числа. Напишите программу, которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно.

number_a, number_b, number_c = map(int, input('Введите через пробел три числа: ').split())
if number_a > number_b:
    if number_a > number_c:
        print(number_a)
    else:
        print(number_c)
else:
    if number_b > number_c:
        print(number_b)
    else:
        print(number_c)
