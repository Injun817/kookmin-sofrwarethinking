import sys

input = sys.stdin.readline # 정 모르겠어서 찾아본거

a, b = map(int, input().split())
y = 0
accom = {}
for i in range(b):
    num = input().rstrip() #이거 안 넣으면 \n이 추가된다고 함(readline)
    if num in accom:
        del accom[num]
    accom[num] = 1

for key in accom:
    print(key)
    y += 1
    if(y == a):
        break