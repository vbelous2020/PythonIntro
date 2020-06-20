"""
Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
Небольшая подсказка. В этой задаче вам понадобится:
    - список
    - метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не придётся разворачивать
    список), чтоб развернуть список, метод `join()`
    - строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт `from string import
    ascii_uppercase`), она содержит все буквы латинского алфавита.
"""


def converter_func(num, system):
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tmp = []
    while num > 0:
        r = num % system
        tmp.insert(0, s[r])
        num //= system
    res = ''.join(tmp)
    return res


print(converter_func(123456, 2))
