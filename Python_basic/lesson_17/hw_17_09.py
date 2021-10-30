'''
Задача 9. Список списков
Дан вот такой (уже многомерный!) список:
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
Напишите код, который «раскрывает» все вложенные списки, то есть оставляет только внешний список.
Для решения используйте только list comprehensions.
Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
'''
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
nice_list_2 = [nice_list[j][x][y] for j in range(2) for x in range(3) for y in range(3)]
print(nice_list)
print(nice_list_2)

nice_list_1 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
nice_list_21 = [z for x in nice_list_1 for y in x for z in y]
print(nice_list_21)
