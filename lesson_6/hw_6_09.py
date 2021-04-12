# Задача 9. Игра «Угадай число»
# В одном из домашних заданий мы делали задачу, где папа-программист написал для сына программу,
# которая просит его угадать число. Недостаток программы был в том, что бедному сыну приходилось её каждый раз перезапускать,
# чтобы угадывать число. Теперь, когда мы знаем гораздо больше, пришло время исправить этот недостаток и заодно немного улучшить саму игру.
# Напишите программу-игру, которая запрашивает у пользователя число до тех пор, пока он его не отгадает.
# Выводите сообщения в соответствии с примером.
# Пример (загадали число 7):
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4

x_number = 8
attempt_counter = 0
while True:
    attempt_counter += 1
    your_number = int(input('Введите число: '))
    if x_number > your_number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    elif x_number < your_number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    else:
        print(f'Вы угадали! Число попыток: {attempt_counter}')
        break
