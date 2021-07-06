"""
Задача 10. Сортировка (по желанию)
Дан список из N чисел. Напишите программу,
которая сортирует элементы списка по возрастанию и выводит его на экран.
Дополнительный список не использовать.
Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.

Пример:
Изначальный список: [1, 4, -3, 0, 10]
Отсортированный список: [-3, 0, 1, 4, 10]
"""


def sort_list(number_list):
    '''Функция принимает список и возвращает сортированый список.'''
    for i in range(0, len(number_list), 1):
        for j in range(i, len(number_list), 1):
            if number_list[i] > number_list[j]:
                temp = number_list[i]
                number_list[i] = number_list[j]
                number_list[j] = temp
    return number_list


def creator():
    """Функция принимает от пользователя числа и возвращает список."""
    number_list = list(map(int, input('Введите числа через пробел: ').split()))
    return number_list


if __name__ == '__main__':
    a = creator()
    print(sort_list(a))
