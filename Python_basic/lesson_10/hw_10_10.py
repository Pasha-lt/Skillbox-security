print('Задача 10. Яма ')

# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

n = int(input('Введите число: '))
for line in range(n):
    step = n - line
    for left_number in range(n, step - 1, -1):
        print(left_number, end='')
    point = 2 * (step - 1)
    print('.' * point, end='')
    for right_number in range(step, n + 1):
        print(right_number, end='')
    print()
