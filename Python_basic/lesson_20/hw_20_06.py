'''
Задача 6. По парам
Есть список из 10 случайных чисел. Напишите программу,
которая делит эти числа на пары кортежей внутри списка, и выведите результат на экран.
Дополнительно: решите задачу несколькими способами.
Пример:
Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
'''
import random

list_random = [random.randrange(1, 100) for i in list(range(10))]
list_random_2 = [random.randrange(1, 100) for i in list(range(10))]

finish_list = []
finish_list_2 = []

# solution 1
temporary_list = []
for number, element in enumerate(list_random):
    if number % 2 != 0:
        temporary_list.append(element)
        finish_list.append(tuple(temporary_list))
        temporary_list = []
    else:
        temporary_list.append(element)

# solution 2
while len(list_random_2) > 1:
    finish_list_2.append((list_random_2[0], list_random_2[1]))
    list_random_2 = list_random_2[2:]

print(finish_list)
print(finish_list_2)
