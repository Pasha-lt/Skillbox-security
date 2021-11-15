'''
Задача 10 (по желанию). Снова палиндром
Пользователь вводит строку. Необходимо написать программу, которая определяет,
существует ли у этой строки такая перестановка, при которой она станет палиндромом.
Выведите соответствующее сообщение.

Пример 1:
Введите строку: aab
Можно сделать палиндромом

Пример 2:
Введите строку: aabc
Нельзя сделать палиндромом
'''


def is_polyndrom(us_string):
    char_dict = {}
    for i_sym in us_string:
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1
    
    odd_count = 0
    for i_value in char_dict.values():
        if i_value % 2 != 0:
            odd_count += 1
    
    return odd_count <= 1

assert is_polyndrom('aab')
assert not is_polyndrom('aaab')
assert is_polyndrom('aabbc')
