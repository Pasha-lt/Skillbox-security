"""
Задача 7. Двумерный список
Как мы говорили ранее, в программировании часто приходится писать код исходя из результата,
который требует заказчик. В этот раз заказчику нужно получить вот такой двумерный список:
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
Напишите программу, которая генерирует такой список и выводит его на экран.
Используйте только list comprehensions.
"""
# first solution
list_1 = [[1] for i in range(1,5)]
[list_1[i].append((i)+4+list_1[i][0]) for i in range(4)]
[list_1[i].append((i)+8+list_1[i][0]) for i in range(4)]


# second solution
list_3 = [[1] for i in range(1,5)]
[list_3[i].append((j+1)*4+i+list_3[i][0]) for i in range(4) for j in range(2)]


# first solution
list_1 = [[1] for i in range(1, 5)]
[list_1[i].append((i) + 4 + list_1[i][0]) for i in range(4)]
[list_1[i].append((i) + 8 + list_1[i][0]) for i in range(4)]

# second solution
list_3 = [[1] for i in range(1, 5)]
[list_3[i].append((j + 1) * 4 + i + list_3[i][0]) for i in range(4) for j in range(2)]


# third solution
new_list = [[elem for elem in range(n, n + 12, 4)] for n in range(1, 5)]
print(new_list)



print(list_1)
print(list_3)
