5-3

for i in range(5): #층에 따라 range를 맞춤
    if i == 0 or i == 4:
        stars = '*' * 5
        spaces = ' ' * 0
    else:
        stars = '*' * 1
        spaces = ' ' * 8
    line = stars + spaces + stars
    print(line)