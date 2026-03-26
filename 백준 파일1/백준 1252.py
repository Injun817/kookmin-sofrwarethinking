a, b = map(str, input().split())
n1 = int(a, 2)
n2 = int(b, 2)
n3 = n1+n2
print(bin(n3)[2:])
