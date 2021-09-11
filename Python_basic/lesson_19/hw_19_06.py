'''
Задача 6. Словарь синонимов
Одна библиотека поручила вам написать программу для оцифровки словарей слов-синонимов.
На вход в программу подаётся N пар слов. Каждое слово является синонимом к парному ему слову.
Реализуйте код, который составляет словарь слов-синонимов (все слова в словаре различны),
затем запрашивает у пользователя слово и выводит на экран его синоним. Обеспечьте контроль ввода:
если такого слова нет, то выведите ошибку и запросите слово ещё раз.
При этом проверка не должна зависеть от регистра символов.

Пример:
Введите количество пар слов: 3
1 пара: Привет - Здравствуйте
2 пара: Печально - Грустно
3 пара: Весело - Радостно
Введите слово: интересно
Такого слова в словаре нет.
Введите слово: здравствуйте
Синоним: Привет
'''

# dictionary_word = {'Привет':'Здраствуйте', 'Печально':'Грустно', 'Весело':'Радостно'}
dictionary_word = {}

word_count = int(input('Введите количество пар слов: '))
for i in range(word_count):
    new_word = input('{} пара: '.format(i+1))
    key, value = new_word.split(' - ')
    dictionary_word[key] = value

word_check = input('Введите слово: ').title()
# word_check = word_check.title()
print(word_check)
#to do Проверку сделать


check_list_words = []
for k, y in dictionary_word.items():
    check_list_words.append(k)
    check_list_words.append(y)
# check_list_words = [f'{k, y}' for k,y in dictionary_word.items()]

if word_check in check_list_words:
    for key_d, value_d in dictionary_word.items():
        if word_check == key_d:
            print('Синоним: {}'.format(value_d))
        elif word_check == value_d:
            print('Синоним: {}'.format(key_d))
elif word_check not in check_list_words:
    print('Такого слова в словаре нет.')
