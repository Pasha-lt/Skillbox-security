# Задача 3. Слишком большие числа
# У неудачливого бухгалтера всё опять идёт наперекосяк: ему приносят такие большие счета, что числа не помещаются на бумаге.
# Напишите программу, которая считала бы для него, сколько десятичных цифр (знаков) во вводимом числе.

number = int(input('Введите число: '))
count = 1
while True:
    if number < 10:
        break
    number = number//10
    count += 1

print(count)