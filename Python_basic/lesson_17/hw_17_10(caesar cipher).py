"""
Задача 10. Шифр Цезаря (сделайте по желанию)
Юлий Цезарь использовал свой способ шифрования текста.
Каждая буква заменялась на следующую по алфавиту через K позиций по кругу.
Если взять русский алфавит и k = 3, то в слове, которое мы хотим зашифровать,
буква А станет буквой Г, Б станет Д и так далее.
Пользователь вводит сообщение, а также значение сдвига. Напишите программу,
которая зашифрует это сообщение при помощи шифра Цезаря.
Пример:
Введите сообщение: это питон
Введите сдвиг: 3
Зашифрованное сообщение: ахс тлхср
"""


def caeser_cipher(string, user_step):
    cahr_list = [(alphabet[(alphabet.index(alpha) + user_step) % 26] if alpha != ' ' else ' ') for
                 alpha in string]
    new_str = ''
    for i_char in cahr_list:
        new_str += i_char
    return new_str


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
user_string = input('Введите сообщение: ')
step = int(input('Введите сдвиг: '))

output_str = caeser_cipher(user_string, step)
print(output_str)
