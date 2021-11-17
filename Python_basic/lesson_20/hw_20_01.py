"""
Задача 1. Ревью кода

Ваня работает middle-разработчиком на Python в IT-компании.
Один кандидат на junior-разработчика прислал ему код тестового задания. Задание состояло в следующем:
есть словарь из трёх студентов. Необходимо:

1)Вывести на экран список пар «ID студента — возраст».
2)Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения:
полный список интересов всех студентов и общую длину всех фамилий студентов.
3)Далее в основном коде эта функция вызывается, и значения присваиваются отдельным переменным,
которые после выводятся на экран. (Т.е. нужно распаковать все возвращаемые значения в отдельные переменные.)

Ваня — очень придирчивый программист, и после просмотра кода он понял,
что этого кандидата на работу не возьмёт, даже несмотря на то, что он выдаёт верный результат.
Вот сам код кандидата:



students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },

    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },

    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0

    for s in string:
        cnt += 1
    return lst, cnt

pairs = []
for i in students:
    pairs += (i, students[i]['age'])

my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)


Перепишите этот код так, чтобы он был максимально pythonic и Ваня мало к чему мог придраться
(ну только если очень захочется). Убедитесь в том, что программа работает всё так же верно.
Различные проверки на существование записей в словаре не обязательны, но приветствуются :)
"""
STUDENTS = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def handle_students_dict(students_dict):
    """
    Функция принимает словарь с информацией по студентам и возвращает список из хобби и
    общее количество букв в фамилиях студентов.
    :param students_dict:dict
    :return list_hobby: list - список хоби студентов 
    :return surname_letters_count: int - общее количество букв в фамилиях студентов
    """
    list_hobby = []
    surname_letters_count = 0
    for i in students_dict:
        list_hobby.extend(students_dict[i]['interests'])
        surname_letters_count += len(students_dict[i]['surname'])
    
    return list_hobby, surname_letters_count


list_hobb, surname_letters_coun = handle_students_dict(STUDENTS)
print(list_hobb, surname_letters_coun)
