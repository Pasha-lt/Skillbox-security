print('Задача 4. Урок информатики 3')


# Наконец-то учитель смог объяснить детям,
# что такое эта «плавающая точка». Однако долго его радость не продлилась,
# ведь на следующем уроке нужно будет объяснить такие страшные слова,
# как «экспоненциальное», «мантисса» и «порядок».

# Хоть старшеклассники и знакомы с экспонентой,
# учитель всё равно не уверен, что здесь всё будет понятно.
# Поэтому для наглядности он также написал программу.

# На вход подаётся строка — это экспоненциальная форма числа.
# Напишите программу,
# которая выводит отдельно мантиссу и отдельно порядок этого числа.


def expo_number_f(expo_number):
    order = 0
    if float(expo_number) >= 10:
        for numeral in expo_number:
            if numeral == '0':
                order += 1
            elif numeral == '.':
                break
        expo_number = float(expo_number) / (10 ** order)

    elif 0 < float(expo_number) < 1:
        for numeral in expo_number:
            if numeral != '0' and numeral != '.':
                break
            else:
                order += 1
        expo_number = '0.' + expo_number[order:]
        order = (order - 1) * -1
        expo_number = float(expo_number) * 10

    return f'Мантиса: {expo_number}\nПорядок: {order}'


expo_number = input('Введите экспоненциальная форма числа: ')
print(expo_number_f(expo_number))
