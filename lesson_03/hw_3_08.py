# Реализуйте программу, которая получает на вход четырёхзначное число и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных.

number = int(input('Введите число: '))
first_number = number//1000
second_number = number//100%10
third_number = number//10%10
fourth_number = number%10

print(first_number)
print(second_number)
print(third_number)
print(fourth_number)
