"""
# Задача 5. Песни
#
# Мы пишем приложение для удобного прослушивания музыки.
# У Вани есть список из девяти песен группы Depeche Mode.
# Каждая песня состоит из названия и продолжительности с точностью до долей минут:
#
# violator_songs = [
#     ['World in My Eyes', 4.86],
#     ['Sweetest Perfection', 4.43],
#     ['Personal Jesus', 4.56],
#     ['Halo', 4.9],
#     ['Waiting for the Night', 6.07],
#     ['Enjoy the Silence', 4.20],
#     ['Policy of Truth', 4.76],
#     ['Blue Dress', 4.29],
#     ['Clean', 5.83]
# ]
#
# Из этого списка Ваня хочет выбрать N песен и закинуть их в особый плейлист с другими треками.
# И при этом ему важно, сколько времени в сумме эти N песен будут звучать.
#
# Напишите программу, которая запрашивает у пользователя количество песен из списка и затем
# названия этих песен, а на экран выводит общее время их звучания.
#
# Пример:
# Сколько песен выбрать? 3
# Название 1 песни: Halo
# Название 2 песни: Enjoy the Silence
# Название 3 песни: Clean
# Общее время звучания песен: 14.93 минут
"""

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

all_time = 0

amount_song = int(input("Сколько песен выбрать? "))
for number in range(1, amount_song + 1):
    song_name = input(f"Название {number} песни: ")
    for title, time in violator_songs: 
        if title == song_name:
            all_time += time

print(f"Общее время звучания песен: {round(all_time, 2)} минут")

