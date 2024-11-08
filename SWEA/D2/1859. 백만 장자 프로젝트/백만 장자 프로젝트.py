t = int(input())

for i in range(1, t+1):
    day = int(input())
    ans = 0
    num = list(map(int, input().split()))
    price = 0

    for j in num[::-1]:
        if j >= price:
            price = j
        else:
            ans += price - j

    print('#', i, ' ',ans, sep='')