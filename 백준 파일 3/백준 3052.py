a = []
b = 0
for i in range(10):
    c = 0
    a.append((int(input()))%42)
    for j in range(i):
        if(a[j] == a[i]):
            c += 1
    if (c <= 0):
        b+=1
print(b)