'''
Задача 3. Функция
Напишите функцию, которая принимает на вход кортеж и какой-то случайный элемент
(его можно вводить с клавиатуры). Функция должна возвращать новый кортеж,
начинающийся с первого появления элемента в нём и заканчивающийся вторым его появлением включительно.
Если элемента нет вовсе — вернуть пустой кортеж. Если элемент встречается только один раз,
то вернуть кортеж, который начинается с него и идёт до конца исходного.
'''

def foo(user_tuple, user_x):
    if user_x not in user_tuple:
        new_tuple = ()
    else:
        first_index = user_tuple.index(user_x)
        if user_tuple.count(user_x) == 1:
            new_tuple = user_tuple[first_index:-1]
        elif user_tuple.count(user_x) == 2:
            new_tuple = user_tuple[first_index:user_tuple.index(user_x, first_index+1)+1]
        else:
            new_tuple = ('error',)
    return new_tuple

user_tuple = (45,43,56,45,432,54,1,2,1,2,1)
user_x =1

a = foo(user_tuple, user_x)
print(a, type(a))
