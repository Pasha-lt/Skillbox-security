print('Задача 7. Великий и могучий')

# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Особенно Паоло понравилась книга “Преступление и наказание”.
# И ему стало интересно,
# какое можно найти самое длинное слово в этой книге, чтобы потом сравнить его с аналогом на своём языке.
#
# Напишите программу,
# которая получает на вход текст и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.
#
# Пример:
# Введите текст: Меня зовут Петр
# Длина самого длинного слова: 5

users_string = input('Введите текст: ')
count_letter = 0
max_letter = 0
for letter in users_string:
    if letter == ' ':
        count_letter = 0
    else:
        count_letter +=1
        if count_letter > max_letter:
            max_letter = count_letter

print(f'Длина самого длинного слова: {max_letter}')
