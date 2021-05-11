print('Задача 1. Урок информатики 2')

# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
#
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
#
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
#
# Пример 1:
#
# Введитечисло: 92345
#
# Формат плавающей точки: x = 9.2345 * 10 ** 4
#
# Пример 2:
#
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3


order = 0
number_entered = result = float(input('Введите число:'))
if number_entered >= 10:
    while number_entered >= 10:
        order += 1
        number_entered //= 10
    result /= (10 ** order)
elif 0 < number_entered < 1:
    while number_entered < 1:
        order -= 1
        number_entered *= 10
    result /= (10 ** order)
print('Формат плавающей точки: х =', result, '* 10 **', order)