n = int(input('Введите количество школьников: '))
print(n)
k = int(input('Введите количество яблок: '))
print(k)

quantity = k // n
print('Количество яблок на каждого ученика:', quantity)
rest = k - (n * quantity)
print('Останется в корзинке:', rest)
