'''
Задача 7. Функция сортировки
Напишите функцию, которая сортирует кортеж, состоящий из целых чисел, по возрастанию и возвращает его.
Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.
'''


def tuple_sort(user_tuple):
    new_tuple = ()
    for number in sorted(list(user_tuple)):
        if type(number) == int:
            new_tuple = new_tuple + (number,)
        else:
            return user_tuple
    return new_tuple


my_tuple = (5, 1.1, 2, 4, 3)
print(tuple_sort(my_tuple))
