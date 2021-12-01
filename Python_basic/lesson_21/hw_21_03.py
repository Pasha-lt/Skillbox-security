"""
Задача 3. Ряд Фибоначчи
Числа Фибоначчи — это ряд чисел, в котором каждое следующее число равно сумме двух предыдущих:
1, 1, 2, 3, 5, 8, 13, …
Пользователь вводит num_pos. Напишите функцию, которая выводит число,
которое стоит на позиции num_pos в ряде Фибоначчи.
Пример 1:
Введите позицию числа в ряде Фибоначчи: 6
Число: 8
Пример 2:
Введите позицию числа в ряде Фибоначчи: 10
Число: 55
"""

def fibonacci(stop_number, list_a):
    if len(list_a) == stop_number:
        return list_a[-1]
    else:
        list_a.append(list_a[-1]+list_a[-2])
    return fibonacci(stop_number, list_a)

list_a = [1,1]
stop_number = int(input('Введите число: '))
print(fibonacci(stop_number, list_a))
