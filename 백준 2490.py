a, b, c, d = map(int, input().split()) #그냥 반복문 3번 쓸 것
a1, b1, c1, d1 = map(int, input().split())
a2, b2, c2, d2 = map(int, input().split())
if(a+b+c+d == 4):
    print("E")
elif(a+b+c+d == 3):
    print("A")
elif(a+b+c+d == 2):
    print("B")
elif(a+b+c+d == 1):
    print("C")
else:
    print("D")
if(a1+b1+c1+d1 == 4):
    print("E")
elif(a1+b1+c1+d1 == 3):
    print("A")
elif(a1+b1+c1+d1 == 2):
    print("B")
elif(a1+b1+c1+d1 == 1):
    print("C")
else:
    print("D")
if(a2+b2+c2+d2 == 4):
    print("E")
elif(a2+b2+c2+d2 == 3):
    print("A")
elif(a2+b2+c2+d2 == 2):
    print("B")
elif(a2+b2+c2+d2 == 1):
    print("C")
else:
    print("D")