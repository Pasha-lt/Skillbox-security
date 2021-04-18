# Задача 7. Отрезок
# Напишите программу, которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

sum_grade = 0
counter_grade = 0

number_a = int(input('Введите число а: '))
number_b = int(input('Введите число б: '))

for number in range(number_a, number_b + 1):
    if not number % 3:
        print(number)
        sum_grade += number
        counter_grade += 1

print(round(sum_grade / counter_grade, 1))
