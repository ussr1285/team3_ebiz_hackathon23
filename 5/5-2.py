for i in range(7): #층에 따라 range를 맞춤
    if 8-(2*i) >= 2: #stars의 개수가 2이상이면 첫번째 식
        spaces = ' ' * (i)
        stars = '*' * (8 - (2*i))
    else: #stars의 개수가 2 미만일땐 두번째 식 적용
        spaces = ' ' * (6- i)
        stars = '*' * (2*i - 4)
    line = spaces + stars + spaces
    print(line)
