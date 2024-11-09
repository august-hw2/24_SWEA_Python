t = int(input())

for case in range(1, t+1):
    length = int(input())
    pascal = []
    for i in range(0, length):
        tmp = []
        for j in range(0, length):
            tmp.append(0)
        pascal.append(tmp)

    pascal[0][0] = 1

    for i in range(1, length):
        for j in range(0, length):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print('#{}'.format(case))
    for i in range(0, length):
        for j in range(0, length):
            if pascal[i][j] != 0:
                print(pascal[i][j], end=' ')
        print()