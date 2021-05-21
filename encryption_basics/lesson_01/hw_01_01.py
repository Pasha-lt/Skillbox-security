# 1. Открытое сообщение написано на английском языке. Расшифруйте фразу, в ответе также укажите ключ шифра.
#
# VG HFRQ GB OR RKCRAFVIR GB ZNXR GUVATF CHOYVP NAQ PURNC GB ZNXR GURZ CEVINGR ABJ VGF RKCRAFVIR GB
# ZNXR GUVATF CEVINGR NAQ PURNC GB ZNXR GURZ CHOYVP

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
# c2=p15, b1 = o14 n13= a1

encription_string = 'VG HFRQ GB OR RKCRAFVIR GB ZNXR GUVATF CHOYVP NAQ PURNC GB ZNXR GURZ CEVINGR ABJ VGF RKCRAFVIR GB ZNXR GUVATF CEVINGR NAQ PURNC GB ZNXR GURZ CHOYVP'

# самая распространненая буква в английском языке 'e' найдем самую часто повторяющуюся букву в нашей последовательности.
count_alpha = {}  # Делаем словарь где ключами будут буквы, а значениями количество букв в строке.
for alpha in encription_string.replace(' ', ''):
    if alpha in count_alpha:
        count_alpha[alpha] += 1
    else:
        count_alpha[alpha] = 1

sort_list = [count for count in count_alpha.values()]
sort_list.sort()  # сортируем чтобы узнать количество максимальных и минимальных повторов. Минимальные '0' максимальной '-1'
# print(sort_list)

count_alpha_count_key = {value: key for key, value in count_alpha.items()}  # делаем генератор словарей чтобы ключами
# выступали количество повторов. Так как они могут повторятся и из-за этого будет сбой нужно проверить.

# print(count_alpha_count_key[sort_list[0]])  # самая редкая
# print(count_alpha_count_key[sort_list[-1]])  # самая частая
most_popular_alpha = alphabet_list.index(
    count_alpha_count_key[sort_list[-1]].lower())  # находим под каким номером у нас самая часто употребляемая буква
slide_order = most_popular_alpha - alphabet_list.index(
    'e')  # находим разницу между самой популярной букву шифра и 'е' это и будет нужный нам степ.

decode_string = ''
for i in encription_string.lower():
    if i == ' ':
        decode_string += ' '  # меняем пробелы на нижнее подчеркивание
    elif alphabet_list.index(i) < slide_order:  # Если индекс буквы в алфавите меньше 13 тогда добавляем 13
        decode_string += alphabet_list[alphabet_list.index(i) + slide_order]
    else:  # Если индекс буквы в алфавите больше 13 тогда минусуем 13
        decode_string += alphabet_list[alphabet_list.index(i) - slide_order]

print(decode_string)
