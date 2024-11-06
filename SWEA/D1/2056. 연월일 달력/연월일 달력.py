T = int(input())
for test_case in range(1, T + 1):
    date = str(input())
    year, month, day = date[:4], date[4:6], date[6:]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 0<int(month)<13 and int(day) <= days[int(month)-1]:
        print('#{} {}/{}/{}'.format(test_case, year, month, day))
    else:
        print('#{} {}'.format(test_case, -1))