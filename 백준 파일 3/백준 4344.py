n = int(input())
num = []
for i in range(n):
    a = input().split()
    b=0
    c = 0
    for j in range(int(a[0])):
        b += int(a[j+1])
    for j in range(int(a[0])):
        if (int(a[j+1])>(b/(int(a[0])))):
            c += 1
    num.append(round((c*100)/int(a[0]), 3))
for i in range(n):
    print(f"{num[i]:.3f}%")
