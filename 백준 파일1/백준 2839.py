n = int(input())
temp = 0
temp_1 = 10000
if((n%5)==0):
    temp = n//5
else:
    for i in range((n//5), -1, -1):
        temp_2 = 0
        num1 = n-(5*i)
        temp_2 += i
        if(num1 % 3 == 0):
            num2 = num1 // 3
            temp_2 += num2
            if(temp_1 >= temp_2):
                temp_1 = temp_2
        else:
            continue
    if (temp_1==10000):
        temp = -1
    else:
        temp = temp_1
print(temp)
