"""
Задача 1. Генерация списка
Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от 1 до N.
"""
        
N = int(input("Введите число"))
final_list = []
[final_list.append(n) for n in range(1,N) if n%2==0]
print(final_list)
