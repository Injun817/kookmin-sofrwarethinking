num = int(input())
dic = {}
for i in range(num):
    name = input()
    if( dic.get(name) == None):
        dic.update({name:1})
    else:
        a = int(dic.get(name))+1
        del dic[name]
        dic.update({name:a})
name = dict(sorted(dic.items()))
a = 0
for key in name:
    if(a<int(name[key])):
        a = int(name[key])
        b = key
print(b)