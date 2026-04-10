a = int(input())
num = []
for i in range(a):
    b = int(input())
    if(b==0):
        num.pop()
    else:
        num.append(b)
c = 0
for i in range(len(num)):
    c += num[i]
print(c)