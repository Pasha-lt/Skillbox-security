"""
Задача 5. Разворот

На вход в программу подаётся строка, в которой буква h встречается как минимум два раза.
Реализуйте код, который разворачивает последовательность символов,
заключённую между первым и последним появлением буквы h, в противоположном порядке.
"""

user_string = 'jhopkldh'
first_h = user_string.find('h')
last_h = user_string.rfind('h')
print(user_string[last_h - 1:first_h:-1])