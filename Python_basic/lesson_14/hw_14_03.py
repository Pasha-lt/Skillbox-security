# Задача 3. Сумма и разность
# Напишите две функции: первая принимает одно целое положительное число N и находит сумму всех цифр числа N;
# вторая принимает число N и считает количество цифр в числе. В ответе выводится разность суммы чисел и количества.
# Пример работы программы:
# Введите число: 500
# Сумма цифр: 5
# Кол-во цифр в числе: 3
# Разность суммы и кол-ва цифр: 2

from functools import reduce

def sum_numbers(n):
    return reduce(lambda x, y: int(x) + int(y), n)

def count_numbers(n):
    return len(n)

n = input('Введите число: ')

sum_numbers_velue = sum_numbers(n)
count_numbers_value = count_numbers(n)

print(f'Сумма цифр: {sum_numbers_velue}\nКол-во цифр в числе: {count_numbers_value}\nРазность суммы и кол-ва цифр: {sum_numbers_velue - count_numbers_value}')
