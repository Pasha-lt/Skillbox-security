"""
Задача 2. Шеренга
Два класса стоят в две отдельные шеренги. В каждом классе ученики выстроены по росту
(по возрастанию): в одном классе от 160 см до 176 см с шагом 2, во втором классе — от 162 см
до 180 см с шагом 3. Спустя какое-то время два класса объединяют в одну шеренгу и
тоже выстраивают их по возрастанию.
Напишите программу, которая генерирует списки роста для каждого в классе,
затем объединяет их в один список и сортирует его в порядке возрастания.
Выведите отсортированный список на экран.
"""


def creator_pupil():
    """This function create pupils and return two lists"""
    first_class = [height for height in range(160, 176, 2)]
    second_class = [height for height in range(162, 180, 3)]
    return first_class, second_class


def mix_and_sort_pupils(first_class, second_class):
    """This function mix two lists and after that sort it and return sorted list"""
    first_class.extend(second_class)
    first_class.sort()
    return first_class


if __name__ == '__main__':
    a, b = creator_pupil()
    print(mix_and_sort_pupils(a, b))
