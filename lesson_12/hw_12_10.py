print('Задача 10')


# Напишите игру - текстовый квест.
# Игрок находится в квартире, его задача - покинуть ее.
#
# Игрок свободно перемещается по квартире, пока не покинет ее.
#
# В квартире есть три комнаты (спальня, кухня, ванна) и коридор.
# В ванну можно попасть из коридора и спальни.
# В спальню можно попасть из ванны и коридора.
# На кухню можно попасть только из коридора.
# Коридор связан со всеми комнатами, но в нем дополнительно есть дверь наружу.
# На кухне открыто окно.
# Если игрок пытается выбраться через него, то разбивается и проигрывает


# Пример:

# Вы в спальне. Куда идем?
# 1 - в ванну
# 2 - в коридор

# 2

# Вы в коридоре. Куда идем?
# 1 - в спальню
# 2 - в ванну
# 3 - на кухню
# 4 - в дверь

# 2

# Вы в ванне. Куда идем?
# 1 - в коридор
# 2 - в спальню

# 2

# Вы в спальне...

def hall():
    print('Вы в коридоре. Куда идем?\n'
          '1 - в спальню\n'
          '2 - в ванну\n'
          '3 - на кухню\n'
          '4 - в дверь')
    choice = int(input())
    if choice == 1:
        bedroom()
    elif choice == 2:
        bathroom()
    elif choice == 3:
        kitchen()
    elif choice == 4:
        print('Вы вышли на улицу. Конец игры!')
    else:
        print('Введите другую команду!')


def bedroom():
    print('Вы в спальне. Куда идем?\n'
          '1 - в ванну\n'
          '2 - в коридор\n')
    choice = int(input())
    if choice == 1:
        bathroom()
    elif choice == 2:
        hall()
    else:
        print('Введите другую команду!')


def kitchen():
    print('Вы на кухне. Куда идем?\n'
          '1 - в коридор\n'
          '2 - в окно\n')
    choice = int(input())
    if choice == 1:
        hall()
    elif choice == 2:
        window()
    else:
        print('Введите другую команду!')


def bathroom():
    print('Вы в ванне. Куда идем?\n'
          '1 - в коридор\n'
          '2 - в спальню\n')
    choice = int(input())
    if choice == 1:
        hall()
    elif choice == 2:
        bedroom()
    else:
        print('Введите другую команду!')


def window():
    print('Вы вылезли в окно. Куда идем?\n'
          '1 - вернуться на кухню\n'
          '2 - прыгнуть')
    choice = int(input())
    if choice == 1:
        kitchen()
    elif choice == 2:
        print('Вы выпругнули из окна и разбились(')
    else:
        print('Введите другую команду!')


hall()
