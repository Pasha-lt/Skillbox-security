# Задача 9. Выражение
# Дано число x. Напишите программу для вычисления следующего выражения
# (x-1)/(x-2) * (x-3)/(x-4) * .... * (x-63)/(x-64)

x = int(input("Введите x: "))
final_score = 1
for number in range(1, 7):
    final_score *= (x - ((2 ** number) - 1)) / (x - (2 ** number))
print(final_score)
