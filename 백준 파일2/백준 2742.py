
a, b = map(int, input().split())
num = []
num.append(map(int, input().split()))
for i in range(0, a):
    if(num[i] >= b):
        num.extend(num[i])
print(num)