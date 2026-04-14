a = int(input())
b = int(input())

num = set()
for i in range(2, 101):
    for j in range(i*2, 10001, i):
        num.add(j)
prime_num = sorted(list(set(range(2, 10001))-(num)))
c = 0
d = 0
for i in range(a, b+1):
    if(i in prime_num):
        c+=i
        if(d == 0):
            d = i
if(c == 0):
    print(-1)
else:
    print(c)
    print(d)