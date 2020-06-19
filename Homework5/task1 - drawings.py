"""
rows = 11
cols = 11

for i in range(rows):
    for j in range(cols):
        if i == cols or j == i or :
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()

#x == width / 2 or y == width / 2 - x or y == width / 2 + x
#i == 0 || j == i || j == cols - i
"""
# x == width / 2 - y or x == width / 2 + y or y == width / 2 + x or x == (width - y) + width / 2

height = 11
width = 11
# Треугольник
for x in range(width):
    for y in range(height):
        if x == width//2 or y == width//2 - x or y == width//2 + x:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()


# Ромб
for x in range(width):
    for y in range(height):
        if x == width // 2 - y or x == width // 2 + y or y == width // 2 + x or x == width-1 - y + width // 2:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()

