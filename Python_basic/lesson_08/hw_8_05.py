# Задача 5. Функция 2
# В прошлый раз мы написали Саше программу, которая считает функцию в каждой точке отрезка и выводит значение на экран. Но теперь ему нужно, чтобы значения считались в обратном порядке. Плюс к этому в программе ему нужно сделать так, чтобы можно было настраивать шаг, с которым он скачет по точкам отрезка.
#
# Напишите программу, которая получает на вход начало и конец отрезка, а также шаг. Затем высчитывает функцию игрек в каждой точке отрезка и с нужным шагом, начиная с конца, и выводит ответ на экран.
#
# Пример:
#
# Введите начало отрезка: -2
# Введите конец отрезка: 2
# Введите шаг: -1
# В точке 2 функция равна 9
# В точке 1 функция равна 0
# В точке 0 функция равна 1
# В точке -1 функция равна 6
# В точке -2 функция равна 9

start_section = int(input("Введите начало отрезка: "))
finish_section = int(input("Введите конец отрезка: "))
step_section = int(input("Введите шаг отрезка: "))

if step_section < 0:
    start_section, finish_section = finish_section, start_section - 2

for x in range(start_section, finish_section + 1, step_section):
    y = x ** 3 + 2 * x ** 2 - 4 * x + 1
    print(f'В точке {x} функция равна {y}')
