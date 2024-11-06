T = list(input())
for i in range(len(T)):
    if T[i].islower():
        T[i] = T[i].upper()

print(''.join(T))