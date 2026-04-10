n = int(input())
num = map(int, input().split())
num = sorted(num)
print(num[0], num[n-1])