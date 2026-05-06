#전치 행렬
import random

n = int(input())

list1 = [[0 for i in range(n)] for j in range(n)] 
list2 = [[0 for i in range(n)] for j in range(n)] 

for i in range(n):
    for j in range(n):
        list1[i][j] = random.randint(1, n*n*10)

for i in range(n):
    for j in range(n):
        list2[j][i] = list1[i][j]

# for i in range(n):
#     for j in range(n):
#         print(f"{list1[i][j]:7d}", end="  ")
#     print("\n")

for i in range(n):
    for j in range(n):
        print(f"{list2[i][j]:7d}", end="  ")
    print("\n")
