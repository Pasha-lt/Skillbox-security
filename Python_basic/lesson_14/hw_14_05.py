# Задача 5. Наименьший делитель
# Дано натуральное число n>1. Напишите функцию, которая находит его наименьший делитель, отличный от 1.
#
# Пример 1:
# Введите число: 6
# Наименьший делитель, отличный от единицы: 2
#
# Пример 2:
# Введите число: 17
# Наименьший делитель, отличный от единицы: 17

def nok(number_nok):
    for step_number in range(2, number_nok+1):
        if number_nok % step_number > 0:
            continue
        else:
            return step_number


number = int(input('Введите число: '))
print(f'Наименьший делитель, отличный от единицы: {nok(number)}')
