# Задача 1. Тайны археологии
# Ирина работает археологом и недавно приехала с интересных раскопок.Там нашли древнюю глиняную табличку,
# на которой еле-еле видны числа 114 12 14 10605 4907 450. Ирина предположила,
# что это такой шифр и хочет использовать программу, которую использовали для расшифровки целой книги из таких чисел.
# Напишите программу, которая проверяет каждое число и выводит к каждому соответствующее сообщение:
# "Число подходит" или "Число не подходит". Число подходит, если оно четное и не делится на 3.

list_number = [114, 12, 14, 10605, 4907, 450]
for number in list_number:
    if number % 3 != 0 and number % 2 == 0:
        print(f'Число {number} подходит')
    else:
        print(f'Число {number} не подходит')
