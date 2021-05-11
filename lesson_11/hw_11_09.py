print('Задача 9. Уравнение')

# Даны действительные коэффициенты a, b, c,
# при этом a≠0.
# Решите квадратное уравнение ax^2+bx+c=0 и выведите все его корни.
#
# Если уравнение имеет два корня,
# выведите два корня в порядке возрастания,
# если один корень — выведите одно число,
# если нет корней — не выводите ничего

a = float(input('Введите число а: '))
b = float(input('Введите число b: '))
c = float(input('Введите число c: '))

discriminant = b ** 2 - 4 * a * c
if discriminant < 0:
    print()
else:
    x1 = (-b + discriminant**0.5)/2*a
    x2 = (-b - discriminant**0.5)/2*a
    if x1 == x2:
        print(x1)
    else:
        print(x1, x2)