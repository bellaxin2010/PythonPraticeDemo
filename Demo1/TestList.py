#-*- coding =utf-8 -*-
# 列表嵌套 ：一个列表包含子列表
import random

teachers = ['x', 'b', 'c', 'd', 'e', 'g', 'h', 'i']
offices = [[], [], []]


for value in teachers:
        num= random.randint(0,2) #下标0，1，2
        #随机到某个列表
        offices[num].append(value)
print(offices)



i=1
for office in offices:
    print(f'办公室{i}老师个数{len(office)}')
    print('老师姓名:')
    for name in office:
        print(name)
    i+=1


