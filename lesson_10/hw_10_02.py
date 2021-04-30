print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


users_number = int(input('Введите число: '))
for row in range(users_number + 1):
    for mult in range(row):
        print(row, end=' ')
    print()

# for row in range(users_number+1):
#     print(str(row) * row)
