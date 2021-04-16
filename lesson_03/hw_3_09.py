# Реализуйте программу, которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке.
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных. Пример ввода: 1234. Пример вывода: 4321.
def reverse_number(number):
    first_number = number // 1000
    second_number = number // 100 % 10
    third_number = number // 10 % 10
    fourth_number = number % 10
    reverse_number = fourth_number*1000+third_number*100+second_number*10+first_number
    print(reverse_number)
    return f'{fourth_number}{third_number}{second_number}{first_number}'


print(reverse_number())
