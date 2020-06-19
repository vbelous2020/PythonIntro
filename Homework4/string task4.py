"""Дана строка. Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и последнего вхождения."""

s = "fh gjdhfjgkhdf jkghdfjghs djfhsdkjhfjdhfkj shf"


i = 0
idx = s.find('h')
while idx >= 0:
    idx = s.find('h', idx+1)
    i += 1

idx = s.find('h', idx+1)
s1 = s[idx+1:].replace('h', 'H', i - 2)
print(s)
s = s[:idx+1] + s1
print(s)


