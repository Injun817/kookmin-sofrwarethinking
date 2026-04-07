a = list(map(int, input().split()))
temp = 0
for i in range(len(a), 0, -1):
    for j in range(0, i-1):
        if(a[j]>a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(a)
