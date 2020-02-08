#-*- encoding=utf-8 -*-

def calc(x):
    return x**2

res = map(calc,[1,4,2,13,5])
res2 = map(lambda x:x**2,[1,3,4,2])
print(res2)
print(res)
map1 =[]
for i in res:
    map1.append(i)

for i in res2:
    map1.append(i)
print(map1)