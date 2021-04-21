# Напишите программу, которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу c.


a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = 3

number_counter = 0
number_sum = 0

for number in range(a, b):
    if not number %3:
        number_sum += number
        number_counter += 1

print(int(number_sum / number_counter))