# Задача 9. Выражение
# Дано число x. Напишите программу для вычисления следующего выражения
# (x-1)/(x-2) * (x-3)/(x-4) * .... * (x-63)/(x-64)

x = int(input("Введите x: "))
final_score = 1

for number in range(1, 65, 2):
    final_score *= (x - number) / (x - number + 1)

print(final_score)
