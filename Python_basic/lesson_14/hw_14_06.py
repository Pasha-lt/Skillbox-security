# # Задача 6. Монетка 2
# Практиканту снова дали задание найти старую металлическую монетку по заданным координатам.
# Но теперь металлоискатель сканирует местность вокруг пользователя в виде круга и при обнаружении/отсутствии металла
# прибор отображает на экране соответствующее сообщение.
# Даны два действительных числа x и y и радиус r. Напишите функцию, которая проверяет, лежит ли точка с координатами (x, y)
# внутри круга с радиусом r (включая его границу). Координаты центра круга — (0, 0). Если точка принадлежит кругу,
# выведите сообщение «Монетка где-то рядом», иначе выведите сообщение «Монетки в области нет».

# Пример 1:
# Введите координаты монетки:
# X: 0.5
# Y: 0.5
# Введите радиус: 1
# Монетка где-то рядом

# Пример 2:
# Введите координаты монетки:
# X: 2
# Y: 2
# Введите радиус: 1
# Монетки в области нет


def search_engine(coord_x, coord_y, radius):
    return coord_y <= radius >= coord_x


print('Введите координаты монетки:')
coord_x = abs(float(input('X: ')))
coord_y = abs(float(input('Y: ')))
radius = float(input('Введите радиус: '))

result = search_engine(coord_x, coord_y, radius)
result = 'Монетка где-то рядом' if result == True else 'Монетки в области нет'
print(result)
