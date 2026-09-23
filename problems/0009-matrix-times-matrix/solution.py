def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    if len(a[0]) != len(b):
        return -1

    c = []

    for row in range(len(a)):
        inter = []
        for col in range(len(b[0])):
            sum = 0
            for num in range(len(b)):
                sum += a[row][num] * b[num][col]
            inter.append(sum)
        c.append(inter)
    

    return c