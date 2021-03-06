'''
Задача 7. IP-адрес 2
При написании клиент-серверного приложения часто приходится работать с теми самыми IP-адресами.
Как мы уже знаем, IP-адрес состоит из четырёх целых чисел в диапазоне от 0 до 255, разделённых точками.
Пользователь вводит строку. Напишите программу, которая определяет,
является ли заданная строка правильным IP-адресом. Обеспечьте контроль ввода,
где предусматривается ввод целых чисел от 0 до 255, а также точки между ними.

Пример 1:
Введите IP: 128.16.35.a4
a4 - не целое число
Пример 2:
Введите IP: 240.127.56.340
340 превышает 255
Пример 3:
Введите IP: 34.56.42,5
Адрес - это четыре числа, разделённые точками
Пример 4:
Введите IP: 128.0.0.255
IP-адрес корректен
'''

user_string = input('Введите IP: ')
user_information = user_string.split('.')

for chunk in user_information:
    if len(user_string) != 4:
        print('Адрес - это четыре числа, разделённые точками')
        break
    elif not chunk.isnumeric():
        print('{} - не целое число'.format(chunk))
    elif int(chunk) > 255:
        print('{} - превышает 255 '.format(chunk))
