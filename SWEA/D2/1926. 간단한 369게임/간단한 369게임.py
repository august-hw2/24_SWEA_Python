n = int(input())
ans = []
for i in range(1, n+1):
    cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if not cnt:
        print(i, end=' ')
    else:
        print('-'*cnt, end=' ')