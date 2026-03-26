import time, math

n = (int(input("자연수>")))

start_time = time.time()
for i in range(2, int(math.sqrt(n)), 1):
    if n % i == 0:
        print("{N}은 {I}로 나누어 떨어집니다.".format(N = n, I = i))
        break
    else:
        print("{N}은 소수입니다.".format(N = n))

print("걸린 시간 :", time.time()-start_time)