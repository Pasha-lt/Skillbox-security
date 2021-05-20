print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

max_value = 0
max_number = 0
sequence = int(input('Введите Длину последовательности: '))
for step in range(sequence):
    number = int(input('Введите число которое вы хотите проверить: '))
    sum_number = 0
    for divider in range(2, number):
        if number % divider == 0:
            break
    else:
        for numeral in str(number):
            sum_number += int(numeral)
        print(sum_number)
        if sum_number > max_value:
            max_value = sum_number
            max_number = number

print(max_number, max_value)
