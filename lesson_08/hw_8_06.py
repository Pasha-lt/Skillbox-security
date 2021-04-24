# Задача 6. Письмо
# У нас есть квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт. Напишите программу, которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт. Размеры письма вводятся с клавиатуры.

# Для квадрата
side_square = int(input('Введите сторону квадрата: '))

counter = 0
while True:
    if side_square > 12:
        counter += 2
        side_square /= 2
    else:
        break
print(counter)

# # Для прямоугольника.
# side_a = int(input('Введите сторону а: '))
# side_b = int(input('Введите сторону b: '))
#
# count = 0
# while True:
#     if side_a < 12 and side_b <12:
#         print(count)
#         break
#     elif side_a > 12 or side_b > 12:
#         count += 1
#         if side_a > side_b:
#             side_a = side_a/2
#         elif side_a < side_b:
#             side_b = side_b / 2
#         else:
#             side_b = side_b / 2
#     else:
#         print(count)
#         break
