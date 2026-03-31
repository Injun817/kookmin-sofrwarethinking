x = int(input())
print(f"       {x}월")
print("일 월 화 수 목 금 토")
y = 0
for i in range(1, x):
    if i <= 7 and (i % 2 == 0) and i != 2:
        y += 30
    elif i == 9 or i == 11:
        y += 30
    elif i == 2:
        y += 28
    else:
        y += 31
z = (y+4)%7+1
if z == 7:
    z = 1
if x <= 7 and (x % 2 == 0) and x != 2:
    print("   "*(z-1), end="")
    for i in range(1, 31):
        if(i<10):
            print(i, end="  ")
        else:
            print(i, end=" ")
        if z>=7:
            print("\n")
            z = 0
        z+=1
elif x == 9 or x == 11:
    print("   "*(z-1), end="")
    for i in range(1, 31):
        if(i<10):
            print(i, end="  ")
        else:
            print(i, end=" ")
        if z>=7:
            print("\n")
            z = 0
        z+=1
elif x == 2:
    print("   "*(z-1), end="")
    for i in range(1, 29):
        if(i<10):
            print(i, end="  ")
        else:
            print(i, end=" ")
        if z>=7:
            print("\n")
            z = 0
        z+=1
else:
    print("   "*(z-1), end="")
    for i in range(1, 32):
        if(i<10):
            print(i, end="  ")
        else:
            print(i, end=" ")
        if z>=7:
            print("\n")
            z = 0
        z+=1
              
        
