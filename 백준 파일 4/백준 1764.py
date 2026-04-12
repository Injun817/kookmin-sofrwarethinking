a, b = map(int, input().split())
name1 = set()
name2 = set()
for i in range(a):
    name = input()
    name1.add(name)
for i in range(b):
    name = input()
    name2.add(name)
name3 = name1 & name2
name = sorted(list(name3))
print(len(name))
for i in range(len(name)):
    print(name[i])