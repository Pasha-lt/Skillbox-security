'''
Задача 2. Универсальная программа 2
Спустя некоторое время заказчик попросил нас немного изменить скрипт для своей криптографии:
теперь индексы элементов должны быть простыми числами.
Напишите функцию, которая возвращает список из элементов итерируемого объекта
(кортежа, строки, списка, словаря), у которых индекс — это простое число.
Для проверки на простое число напишите отдельную функцию is_prime.
Дополнительно: сделайте так,
чтобы основная функция состояла только из оператора return и при этом также возвращала список.
'''


def is_prime(number):
    if number % 2 == 0:
        return number == 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number


def main(array):
    return [value for index_a, value in enumerate(array) if is_prime(index_a)]


def dict_check(array):
    dict_list = []
    if isinstance(array, dict):
        for i in main(array):
            print(i)
            dict_list.append(array[i])
        return dict_list
    else:
        return main(array)


sa = {1: 'sdfdgdf', 3: '4324', 7: 'Пар'}

print(dict_check(sa))
