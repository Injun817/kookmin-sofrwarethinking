n = int(input())
card1 = list(map(int, input().split()))
dic = {}
for i in range(n):
    if card1[i] in dic:
        dic[card1[i]] += 1
    else:
        dic.update({card1[i]:1})

m = int(input())
card2 = list(map(int, input().split()))
for i in range(m):
    id = dic.get(card2[i])
    if(id == None):
        print(int("0"), end=" ")
    else:
        print(id, end=" ")