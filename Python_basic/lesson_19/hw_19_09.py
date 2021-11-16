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

# dict_people = {}
# people_count = int(input('Введите количество человек: '))
# for i in range(people_count):
#     person_1, person_2 = input(f'{i} пара: ').split()
#     dict_people[person_1] = person_2

dict_people = {
    'Alexei': 'Peter_I',
    'Anna': 'Peter_I',
    'Elizabeth': 'Peter_I',
    'Peter_II': 'Alexei',
    'Peter_III': 'Anna',
    'Paul_I': 'Peter_III',
    'Alexander_I': 'Paul_I',
    'Nicholaus_I': 'Paul_I',
}


def step_counter(name, hm):
    if name in dict_people.keys():
        hm += 1
        step_counter(dict_people[name], hm)
    else:
        print(hm)

for i in ['Alexander_I','Alexei','Anna','Elizabeth','Nicholaus_I','Paul_I','Peter_I','Peter_II','Peter_III']:
    print(i)
    step_counter(i, hm=0)
    
# for i in dict_people.keys():
#     step_counter(dict_people[i])
# print(dict_people)
