temp = 0
c = 0
for i in range(0, 4):
    a, b = map(int, input().split())
    c = c+b-a
    if (temp <= c):
        temp = c
print(temp)