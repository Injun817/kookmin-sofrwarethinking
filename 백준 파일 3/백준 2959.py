n = input().split()
# max = 0
# max_num = -1
# max2 = 0
# min = 100
n = sorted(n)
# for i in range(len(n)):
#     if(int(n[i])>=max):
#         max = int(n[i])
#         max_num = i
#     if(int(n[i])<=min):
#         min = int(n[i])
# for i in range(len(n)):
#     if(max2 <= int(n[i]) and max_num != i):
#         max2 = int(n[i])
print(n)
print(int(n[0])*int(n[2])) #정답 : 두번째로 큰 수 x 가장 작은 수