'''
Задача 9. Родословная

В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
Каждому элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
Вам нужно написать программу, которая по заданному генеалогическому древу определяет высоту всех его элементов.
Программа получает на вход N количество человек в генеалогическом древе. Далее следует N−1 строк,
в каждой из которых задаётся родитель для каждого элемента дерева, кроме родоначальника.
Каждая строка имеет вид имя_потомка имя_родителя.

Программа должна вывести список всех элементов древа в лексикографическом порядке (по алфавиту).
После вывода имени каждого элемента необходимо вывести его высоту.

Пример:

Введите количество человек: 9

1 пара: Alexei Peter_I
2 пара: Anna Peter_I
3 пара: Elizabeth Peter_I
4 пара: Peter_II Alexei
5 пара: Peter_III Anna
6 пара: Paul_I Peter_III
7 пара: Alexander_I Paul_I
8 пара: Nicholaus_I Paul_I

“Высота” каждого члена семьи:
Alexander_I 4
Alexei 1
Anna 1
Elizabeth 1
Nicholaus_I 4
Paul_I 3
Peter_I 0
Peter_II 2
Peter_III 2
'''

dict_people = {}
people_count = int(input('Введите количество человек: '))
raw_people_list = []
for i in range(1, (people_count)):
    person_1, person_2 = input(f'{i} пара: ').split()
    raw_people_list.append([person_1, person_2])
    for j in (person_1, person_2):
        if j in dict_people.keys():
            dict_people[j] += 1
        else:
            dict_people[j] = 1

founder = ['test', 0]
for key_2, val_2 in dict_people.items():
    if val_2 > founder[1]:
        founder = [key_2, val_2]

print(raw_people_list)
print(founder)

family_tree = {founder[0]:0}

family_step = 1
while len(raw_people_list):
    for number, pair in enumerate(raw_people_list):
        if pair[1] in family_tree:
            family_tree[pair[0]] = family_step
            del raw_people_list[number]
    family_step += 1

print(family_tree)
#todo доделать

# for name, step in dict_people.items():
#     print(name, step)
