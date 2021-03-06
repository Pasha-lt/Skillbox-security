'''
С увеличением объёма данных возникла потребность в сжатии этих данных,
при этом без потери важной информации. Для этого было придумано кодирование,
которое осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
то есть группы одинаковых символов исходной строки заменяются на этот символ и количество
его повторений в этой позиции строки.
Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и
выводит закодированную последовательность на экран. Кодирование должно учитывать регистр символов.
Пример:
Введите строку: aaAAbbсaaaA
Закодированная строка: a2A2b2с1a3A1
'''

def foo(user_string):
    encryption = 1
    encryption_string =''
    for number, element in enumerate(user_string):
        if number == 0:
            last_symbol = element
        elif number == (len(user_string)-1) and (user_string[-1] != user_string[-2]):
            encryption_string += user_string[-2] + str(encryption)
            encryption_string += user_string[-1] + '1'
        elif number == (len(user_string)-1) and (user_string[-1] == user_string[-2]):
            encryption_string += user_string[-1] + str(encryption+1)
        elif element == last_symbol:
            encryption += 1
            last_symbol = element
        else:
            encryption_string += last_symbol + str(encryption)
            last_symbol = element
            encryption = 1

    return encryption_string

user_string = input('Введите строку: ')
sti = foo(user_string)
print(sti)