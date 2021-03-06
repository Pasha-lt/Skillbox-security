'''
Задача 5. Пароль
При регистрации на сайте помимо логина нужно ещё придумать надёжный пароль.
Этот пароль должен состоять минимум из восьми символов,
в нём должна быть хотя бы одна большая буква и хотя бы три цифры. Тогда он будет считаться надёжным.
Напишите программу, которая запрашивает у пользователя пароль до тех пор,
пока он не введёт надежный пароль. Используется латиница.

Пример:
Придумайте пароль: qwerty
Пароль ненадёжный. Попробуйте ещё раз.
Придумайте пароль: qwerty12
Пароль ненадёжный. Попробуйте ещё раз.
Придумайте пароль: qwerty123
Пароль ненадёжный. Попробуйте ещё раз.
Придумайте пароль: qWErty123
Это надёжный пароль!
'''

def check_password(password):
    digit_counter = 0
    if len(password) >= 8 and password.lower() != password:
        for symbol in password:
            if symbol.isdigit():
                digit_counter += 1
    if digit_counter >= 3:
        return True


while True:
    password = input('Придумайте пароль: ')
    check = check_password(password)
    if check == True:
        print('Это надёжный пароль! ')
        break
    print('Пароль ненадёжный. Попробуйте ещё раз. ')
