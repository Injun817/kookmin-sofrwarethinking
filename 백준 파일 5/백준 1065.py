def han(x):
    c = x//100
    b = (x%100)//10
    a = x%10
    d = a-b
    e = b-c
    if(d==e):
        return 1
    else:
        return 0

n = int(input())
num = 0
if(n<100):
    print(n)
else:
    for i in range(100, n+1):
        if(han(i)==1):
            num += 1
    num += 99
    print(num)