print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!

factorial = 1
number_factorial = int(input('Введите Число с которого нужно вывести факториал: '))

for number in range(2, number_factorial + 1):
    factorial *= number

sum_factorial = factorial

for low_factorial in range(number_factorial, 2, -1):
    sum_factorial += factorial / low_factorial
    factorial = factorial / low_factorial

print(sum_factorial)
