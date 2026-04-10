a = int(input())
num = list(map(int,input().split()))
b = 0
num.sort()
for i in range(a):
    b += num[i]*(i-(a-1-i))
print(b*2)