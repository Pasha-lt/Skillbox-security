'''
Задача 10 (по желанию). Истина

К вам попал зашифрованный текст, означающий большую истину для многих программистов на Python.
Напишите программу, которая реализует алгоритм дешифровки этого текста.
Расшифруйте текст с помощью своей программы, а затем найдите его в интернете.

vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip
'''

encription_string = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'



alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

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
    if i == '/':
        decode_string += '\n'  # меняем пробелы на нижнее подчеркивание
    if i == ' ':
        decode_string += ' '  # меняем пробелы на нижнее подчеркивание

    elif i.isalpha():
        if alphabet_list.index(i) < slide_order:  # Если индекс буквы в алфавите меньше 13 тогда добавляем 13
            decode_string += alphabet_list[alphabet_list.index(i) + slide_order]
        else:  # Если индекс буквы в алфавите больше 13 тогда минусуем 13
            decode_string += alphabet_list[alphabet_list.index(i) - slide_order]
    

print(f'{decode_string}\nШаг шрифта - {slide_order}')
