t = int(input())
ans = []
for i in range(1, int(t**(1/2))+1):
    if t%i == 0:
        ans.append(i)
        if (i**2) != t:
            ans.append(t//i)

ans.sort()
print(*ans)