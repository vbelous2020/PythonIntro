"""
Дан список случайных целых чисел. Замените все нечетные числа списка нулями. И выведете их количество
"""

from random import randint

a = [randint(0, 99) for _ in range(10)]
print(a)

odd = 0

for i in range(len(a)):
    if a[i] % 2 != 0:
        odd += 1
        a[i] = 0

print("Количество нечетных чисел:", odd)
print(a)
print()

"""
Заполните список случайными числами и выполните реверс 
для части списка между элементами с индексами a и b (включая эти элементы)
"""

a = [randint(0, 99) for _ in range(15)]
print(a)
k = int(input('Введите первый индекс: '))
m = int(input('Введите второй индекс: '))
a = a[:k] + a[m:k-1:-1] + a[m+1:]
print(a)
print()


"""
Написать функцию square, принимающую 1 аргумент — сторону квадрата, 
и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
"""


def square(side):
    return 4 * side, side ** 2, round(side * 2 ** (1 / 2))


side = int(input('Введите сторону квадрата: '))
print((square(side)))
print()


"""
Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
 и возвращающую True, если оно простое, и False - иначе.
"""


def is_prime(num):
    if num % 2 == 0:
        return a == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


print(is_prime(int(input('ВВедчите число: '))))
