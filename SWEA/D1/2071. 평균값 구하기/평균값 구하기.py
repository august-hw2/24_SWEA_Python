T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    sum, res = 0, 0
    for i in num:
        sum += i
    res = round(sum/10)
    print('#'+str(test_case), str(res))