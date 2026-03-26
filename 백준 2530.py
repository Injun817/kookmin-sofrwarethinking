a, b, c = map(int, input().split())
time = int(input())
c = c + time%60
temp1 = time//60
if (c>=60):
    c = c-60
    temp1 += 1
b = b + temp1%60
temp2 = temp1//60
if (b>=60):
    b -= 60
    temp2 += 1
a += temp2
if(a>=24):
    a %= 24
print(a, b, c)