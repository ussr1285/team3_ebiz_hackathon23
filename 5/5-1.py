#5-1

for i in range(7, 0, -2):
    line = ' ' * ((7 - i) // 2) + '*' * i + ' ' * ((7 - i) // 2)
    print(line)