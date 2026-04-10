n = int(input())
for i in range(n):
    a = list(input())
    num = 0
    total = 0
    for i in range(len(a)):
        if(a[i] == "O"):
            num += 1
        else:
            num = 0
        total += num
    print(total)
