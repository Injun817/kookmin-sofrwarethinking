n = int(input())

for i in range(0, n):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")