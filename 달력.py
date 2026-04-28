month = int(input())

days = [31,29,31,30,31,30,31,31,30,31,30,31]

day=0
if month>1:

    for i in range(month-1):
        day+=days[i]

day = (day+1)%7

print(f"         {month}")
print(" Su Mo Tu We Th Fr Sa")
print("   "*day,end="")
for i in range(1,days[month-1]+1):
    print(f"{i:3d}",end="")
    if((day+i)%7==0):
        print("\n")
    