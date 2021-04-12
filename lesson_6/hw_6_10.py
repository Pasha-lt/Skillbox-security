# Задача 10. Игра «Компьютер угадывает число»
# Поменяйте мальчика и компьютер из прошлой задачи местами. Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика: «Твое число равно, меньше или больше, чем число N?», где N — число,
# которое хочет проверить компьютер. Мальчик отвечает одним из трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
# Напишите программу, которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

guess_number = 50
max_number = 100
min_number = 0
while True:
    print(guess_number)
    answer = int(input(f'Твое число равно, меньше или больше, чем число {guess_number}? '))
    if answer == 1:
        print('Угадал')
        break
    elif answer == 2:
        min_number =  guess_number
        guess_number = int(guess_number + (max_number - guess_number)/2)
        print(guess_number)
    elif answer == 3:
        max_number = guess_number
        guess_number = int((guess_number + min_number)/2)
        print(guess_number)

