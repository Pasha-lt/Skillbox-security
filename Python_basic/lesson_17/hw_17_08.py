"""
Задача 8. Развлечение
N палочек выставили в один ряд, пронумеровав их слева направо числами от 1 до N.
Затем по этому ряду бросили K камней, при этом i-й камень сбил все палки с номерами от L_i
до R_i включительно. Определите, какие палки остались стоять на месте.
Напишите программу, которая получает на вход количество палок N и количество бросков K.
Далее идёт K пар чисел L_i, R_i, при этом 1≤ L_i≤ R_i≤ N.
Программа должна вывести последовательность из N символов, где j-й символ есть “I”,
если j-я палка осталась стоять, или “.”, если j-я палка была сбита.

Пример:
Кол-во палок: 10
Кол-во бросков: 3
Бросок 1. Сбиты палки с номера 8 по номер 10
Бросок 2. Сбиты палки с номера 2 по номер 5
Бросок 3. Сбиты палки с номера 3 по номер 6

Результат: I.....I...
"""
import random
sticks = int(input('Кол-во палок:  '))
shots = int(input('Кол-во бросков: '))
shots_numbers = []
for j in range(shots):
    k1 = random.randint(1, sticks)
    k2 = random.randint(1, sticks)
    print(f'Бросок {j + 1}. Сбиты палки с номера {min(k1, k2)} по номер {max(k1,k2)}')
    for i in range(min(k1, k2), max(k1,k2) + 1):
        shots_numbers.append(i)
shots_numbers_unic = set(shots_numbers)
sticks_out = [('.' if x in shots_numbers_unic else 'I') for x in range(1, sticks + 1)]
result = ''
for x in sticks_out:
    result += x
print(f'Результат: {result}', end='')