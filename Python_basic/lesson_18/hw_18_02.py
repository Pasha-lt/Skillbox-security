'''
Задача 2. Самое длинное слово
Дана строка, содержащая пробелы. Найдите в ней самое длинное слово,
выведите  это слово и его длину. Если таких слов несколько, выведите первое из них.
'''

user_string = input('Введите свое предложение: ')
new = user_string.split()
new.sort(key=lambda x: len(x))
print(f'Слово - {new[-1]} его длина {len(new[-1])}')
