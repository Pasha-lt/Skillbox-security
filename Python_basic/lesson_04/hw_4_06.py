# Задача 6. Игра в кубики
# Костя играет в азартную игру с кубиками с владельцем заведения. Правда, с довольно интересными правилами:
# если у Кости на кубике выпадет столько же или больше, чем у владельца, то Костя задолжает разность в тысячах долларов.
# Однако если выпадет меньше, то Косте выплатят столько тысяч долларов, сколько будет в сумме очков на кубиках.
# На вход в программу подаётся два числа. Если первое число больше либо равно второму,
# нужно вывести на экран их разность и отдельной строкой фразу: «Костя платит».
# В противном случае вывести их сумму и отдельной строкой — фразу: «Владелец платит».
# Также последней строкой в результате нужно вывести на экран фразу: «Игра окончена».

def cazino(number_a, number_b):
    if number_a >= number_b:
        print(number_b - number_a)
        print('Костя платит')
    else:
        print('Сумма:', number_a + number_b)
        print('Владелец платит')
    print('Игра окончена')


number_a = int(input('Кубик Кости: '))
number_b = int(input('Кубик владельца: '))
cazino(number_a, number_b)
