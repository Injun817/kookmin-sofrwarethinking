n = int(input())
count = 1
a = n//10
b = n%10
num = (b*10)+((a+b)%10)
while(num != n):
    count += 1
    a = num//10
    b = num % 10
    num = (b*10)+((a+b)%10)
print(count)