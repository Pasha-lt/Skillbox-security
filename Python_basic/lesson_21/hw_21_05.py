# ## Задача 5. Ускоряем работу функции
# У нас есть функция, которая делает определённые действия с входными данными:
# 1. Берёт факториал от числа
# 2. Результат делит на куб входного числа
# 3. И получившиеся число возводит в 10 степень
# 
# ````python
# def calculating_math_func(data):
# 	result = 1
# 	for index in range(1, data + 1):
# 		result *= index
# 	result /= data ** 3
# 	result = result ** 10
# 	return result
# ````
# 
# Однако каждый раз нам приходится делать сложные вычисления,
# хотя входные и выходные данные одни и те же. И тут наши знания тонкостей python должны нам помочь.
# 
# Оптимизируйте функцию так, чтобы высчитывать факториал для одного и того же числа только один раз. 
# 
# Подсказка: вспомните что происходит с изменяемыми данными,
# если их выставить по умолчанию в параметрах функции.
# 




from functools import reduce


def calculating_math_func(data):
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    return result


def calculating_math_func2(data):
    result = reduce(lambda x, y: x * y, list(range(1, data + 1)))
    result = (result/ data ** 3)**10
    return result

print(calculating_math_func(5))
print(calculating_math_func2(5))
