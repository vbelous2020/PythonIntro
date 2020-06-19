"""
Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего
параметра функции. Функция должна принимать три параметра: в первом параметре передаётся число для сдвига, второй
параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр задаёт
направление сдвига (по умолчанию влево (False)).
"""


def shift_left(number):
    tmp = number
    d = 0
    amount = 0
    while tmp > 0:
        d = tmp % 10
        tmp //= 10
        amount += 1
    number = number % (10 ** (amount - 1)) * 10 + d
    return number


def shift_right(number):
    tmp = number
    d = tmp % 10
    tmp //= 10
    multi = 1
    while tmp > 0:
        multi *= 10
        tmp //= 10
    number = d * multi + number // 10
    return number


def shift(number, step, direction=False):
    for _ in range(step):
        if direction:
            number = shift_right(number)
        else:
            number = shift_left(number)
    return number


num = 785462354
num = shift(num, 5)
print(num)
print(shift(num, 5, True))