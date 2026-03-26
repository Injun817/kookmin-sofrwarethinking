alp = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
n = list(input())
temp = 0
for i in range(0, len(n)):
    for j in range(0, 52):
        if(n[i] == alp[j]):
            temp += (j+1)
            break
num = 0
for i in range(1, temp):
    if(temp % i == 0):
        num += 1
if(num <= 1):
    print("It is a prime word.")
else:
    print("It is not a prime word.")