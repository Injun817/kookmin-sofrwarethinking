a = int(input())
num = []
for i in range(a):
    num.append(int(input()))
num = sorted(num)
for i in range(a):
    print(num[i])