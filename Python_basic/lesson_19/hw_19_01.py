'''
Задача 1. Песни 2

Мы продолжаем писать приложение для удобного прослушивания музыки,
но теперь наши песни хранятся в виде словаря, а не вложенных списков.
Каждая песня состоит из названия и продолжительности с точностью до долей минут.

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

Напишите программу, которая запрашивает у пользователя количество песен из списка
и затем названия этих песен, а на экран выводит общее время их звучания.

Пример:
Сколько песен выбрать? 3
Название 1 песни: Halo
Название 2 песни: Enjoy the Silence
Название 3 песни: Clean

Общее время звучания песен: 14.93 минут

'''

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

sound_count = int(input('Сколько песен выбрать? '))
user_choise = [input(f'Название  песни {i+1}: ')for i in range(sound_count)]
all_time = [violator_songs[i] for i in user_choise]
print(f'Общее время звучания песен: {round(sum(all_time), 2)} минут')