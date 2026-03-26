n1, n2 = map(int, input().split())

num = []

for i in range(1, n2+1):
    a = str(n1*i)[::-1]
    c = int(a)
    num.append(c)
temp = 0
for i in range(0, n2):
    if(temp <= num[i]):
        temp = num[i]
print(temp)