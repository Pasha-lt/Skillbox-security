print('Задача 8. НОД')


# Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def AverageDiv(first, second):
    if first < second:
        min_a = first
    else:
        min_a = second
    for div in range(1, min_a):
        if first % div == 0 and second % div == 0:
            max_div = div
    print(f'Наибольший общий делитель: {max_div}')


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

AverageDiv(first_number, second_number)


