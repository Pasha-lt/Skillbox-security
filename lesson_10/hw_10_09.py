print('Задача 9. Пирамидка 2')

# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29


height = int(input('Введите личество уровней пирамиды: '))
new_number = 1
for step in range(height):
    print(" " * 4 * (height - step - 1), end='')
    for number in range(step + 1):
        print(new_number, end='    ')
        new_number += 2
    print()
