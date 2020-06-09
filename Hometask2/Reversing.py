n = int(input('Введите положительное, трехзначное число: '))
print('Ваше число:', n)

tmp = n % 10
n_rev = tmp * 100
n1 = n // 10
tmp = n1 % 10
n_rev += tmp * 10
n1 //= 10
n_rev += n1

print('Перевернутое число:', n_rev)

