print('Задача 5. Простые числа')

# Напишите программу,
# которая считает количество простых чисел в заданной последовательности
# и выводит ответ на экран.

counter = 0
sequence = int(input('Введите Длину последовательности: '))
for step in range(sequence):
    number = int(input('Введите число которое вы хотите проверить: '))
    for divider in range(2, number):
        if number % divider == 0:
            break
    else:
        counter += 1

print(f'В вашей последовательность такое количество простых чисел - {counter}')
