a = int(input())
dic = set()
for i in range(a):
    x, y = input().split()
    if(y == "enter"):
        dic.add(x)
    elif(y == "leave"):
        dic.discard(x)
name = sorted(list(dic),reverse=True)
for i in range(len(name)):
    print(name[i])