n = int(input())
for i in range(n):
    a = 0
    b = 0
    paren = list(input())
    for j in range(len(paren)):
        if(paren[j] == "("):
            a += 1
        elif(paren[j]==")"):
            b += 1
        if(a<b):
            break
    if (a == b):
        print("YES")
    else:
        print("NO")