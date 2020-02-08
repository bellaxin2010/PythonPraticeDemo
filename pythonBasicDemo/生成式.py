# -*- encoding=utf-8 -*-

a =[1,3,6,7,8,2]

# 方法1
for index,element in enumerate(a):
    a[index]+=a[index]

print(a)

#方法2：
a = list(map(lambda x:x+x,a))
print(a)

#方法3： 生成式

a= [x+x for x in a]
print(a)
