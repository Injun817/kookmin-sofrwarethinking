import random

n = int(input())
a = [[0 for i in range(n)] for j in range(n)] 
b = [[0 for i in range(n)] for j in range(n)] 
c = [[0 for i in range(n)] for j in range(n)] 
ab = [[0 for i in range(n)] for j in range(n)] 
last  = [[0 for i in range(n)] for j in range(n)] 
for i in range(n):
    for j in range(n):
        a[i][j] = random.randint(1, n*n*10)
        b[i][j] = random.randint(1, n*n*10)
        c[i][j] = random.randint(1, n*n*10)
# print(a)
# print(b)
# print(c)

for i in range(n):
    for j in range(n):
        num = 0
        for k in range(n):
            num += a[i][k] * b[k][j]
        ab[i][j] = num
# print(ab)
for i in range(n):
    for j in range(n):
        last[i][j] = ab[i][j] + c[i][j]
# print(last)
for i in range(n):
    for j in range(n):
        print(f"{last[i][j]:7d}", end="  ")
    print("\n")