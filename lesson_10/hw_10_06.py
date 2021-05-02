print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!

sum_factorial = 1
number_factorial = int(input('Введите Число с которого нужно вывести факториал: '))

for number in range(2, number_factorial + 1):
    sum_factorial *= number

print(sum_factorial)
