def single(x):
    a = x%10
    b=0
    c=0
    d=0
    if (x>=10):
        b = (x//10)%10
    if(x>=100):
        c = (x//100)%10
    if(x>=1000):
        d = (x//1000)%10
    x += (a+b+c+d)
    return x
num = set()
for i in range(1, 10001):
    num.add(i)
single_num = set()
for i in range(1, 10001):
    single_num.add(single(i))
result = sorted(num - single_num)
for i in result:
    print(i)