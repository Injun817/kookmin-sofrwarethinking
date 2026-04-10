n = []
a=-1
max = 0
for i in range(9):
    n.append(int(input()))
    if(n[i]>max):
        max = n[i]
        a = i+1
print(max)
print(a)