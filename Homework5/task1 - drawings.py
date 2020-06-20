
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

