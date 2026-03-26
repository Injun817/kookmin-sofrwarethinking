n = int(input())

for i in range(1, n*2+1):
    for j in range(0, n):
        if((j+i)%2==0):
            print(" ", end="")
        else:
            print("*", end="")
    print("")
        