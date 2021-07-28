# Задача 7. Ролики
# Частная контора даёт в прокат ролики самых разных размеров.
# Человек может надеть ролики любого размера, которые не меньше размера его ноги.
# Пользователь вводит два списка размеров: N размеров коньков и K размеров ног людей.
# Реализуйте код, который определяет,
# какое наибольшее число человек сможет одновременно взять ролики и пойти покататься.

# Пример:
# Кол-во коньков: 4
# Размер 1 пары: 41
# Размер 2 пары: 40
# Размер 3 пары: 39
# Размер 4 пары: 42

# Кол-во людей: 3
# Размер ноги 1 человека: 42
# Размер ноги 2 человека: 41
# Размер ноги 3 человека: 42

# Наибольшее кол-во людей, которые могут взять ролики: 2

skates_counter = int(input('Кол-во коньков: '))
skates_list = []
for number in range(skates_counter):
    new_skate_size = int(input(f'Размер {number + 1} пары: '))
    skates_list.append(new_skate_size)

human_count = int(input('Кол-во людей: '))
human_list = []
for number in range(human_count):
    new_human_size = int(input(f'Размер ноги {number + 1} человека: '))
    human_list.append(new_human_size)

skates_list.sort()
human_list.sort()

suite = 0
for human_size in human_list:
    for skate_size in skates_list:
        if human_size <= skate_size:
            suite += 1
            skates_list.remove(skate_size)
            break

print(f'Наибольшее кол-во людей, которые могут взять ролики: 2')
