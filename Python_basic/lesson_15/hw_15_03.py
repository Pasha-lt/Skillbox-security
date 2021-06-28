'''
Задача 3. Клетки
В научной лаборатории выводят и тестируют новые виды клеток. Есть список из N этих клеток,
где элемент списка — это показатель эффективности, а индекс списка — это ранг клетки.
Учёные отбирают клетки по следующему принципу: если эффективность клетки меньше её ранга,
то эта клетка не подходит. Напишите программу, которая выводит на экран те элементы списка,
значения которых меньше их индекса.
Пример:

Кол-во клеток: 5
Эффективность 1 клетки: 3
Эффективность 2 клетки: 0
Эффективность 3 клетки: 6
Эффективность 4 клетки: 2
Эффективность 5 клетки: 10

Неподходящие значения: 0 2
'''


def user_information():
    """Функция принимает данные от пользователя и возвращает количество клеток и список с данными"""
    number_of_calls = int(input('Кол-во клеток: '))
    calls_list = []
    for index_call in range(1, number_of_calls + 1):
        calls_list.append(int(input(f'Эффективность {index_call} клетки: ')))
    return (calls_list, number_of_calls)


def handler(calls_list, number_of_calls):
    '''Функция принимает список и возвращает список в котором значение меньше индекса списка'''
    list_wrong_calls = []
    for index_call in range(number_of_calls):
        if index_call > calls_list[index_call]:
            list_wrong_calls.append(calls_list[index_call])
    return list_wrong_calls


if __name__ == '__main__':
    print('Неподходящие значения: ', *handler(*user_information()))
