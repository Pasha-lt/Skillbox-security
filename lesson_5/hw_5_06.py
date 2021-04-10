# Задача 6. Защита от дурака
# Мы участвуем в разработке приложения для математиков, где можно будет делать всё,
# начиная от простейших вычислений и заканчивая построением сложных графиков.
# В этом приложении реализована установка диапазона чисел, и нам необходимо написать этакую «защиту от дурака».
# Напишите программу, которая получает на вход число и проверяет, двузначное оно или нет.
# Выведите соответствующее сообщение. Числа −42 и −99 тоже считаются двузначными. Сделайте это,
# используя не более одного оператора if-elsе. Не используйте elif.

def foo(number):
    if (-99 <= number <= 99) and not (-9 <= number <= 9):
        return 'ok'
    else:
        return 'не оk'

# number = int(input('Введите число: '))
assert foo(-1) == 'не оk'
assert foo(100) == 'не оk'
assert foo(-100) == 'не оk'
assert foo(89) == 'ok'
assert foo(00) == 'не оk'
assert foo(5) == 'не оk'
assert foo(-89) == 'ok'
