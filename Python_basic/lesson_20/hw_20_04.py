'''
Задача 4. Игроки
У вас есть словарь игроков, которые участвовали в трёх видах спорта. В словаре хранятся пары «Ф. И. — очки»:

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

Один программист попросил нас для своей базы отправить ему немного другой вариант хранения этой информации.
Напишите программу, которая объединяет ключ словаря со значением в один кортеж, и выведите результат на экран.
Постарайтесь использовать как можно более эффективное решение.
Результат работы программы:
[('Ivan', 'Volkin', 10, 5, 13), ('Bob', 'Robbin', 7, 5, 14), ('Rob', 'Bobbin', 12, 8, 2)]
'''

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# first solution
list_b = []
for i, z in players.items():
    ltemporary_list = []
    for i_1 in i:
        ltemporary_list.append(i_1)
    for z_1 in z:
        ltemporary_list.append(z_1)
    list_b.append(tuple(ltemporary_list))
print(list_b)

#second solution
new = [(name[0], name[1], score[0], score[1], score[2]) for name, score in players.items()]
print(new)
