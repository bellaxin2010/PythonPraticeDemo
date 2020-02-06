#-*- coding：utf-8 -*-

str1 ='01234567895'
print(str1[:5])
print(str1[2:])
print(str1[:])
print(str1[::-1]) # -1 是步长 ， 倒叙排列
print(str1[1:5:1])
print(str1[-4:-1]) #下表-1表示最后一个数据，依次向前类推
print(str1[-4:-1:-1]) #从-4 开始到-1结束，从左到右侧， 但是-1步长，从右到左，方向冲突
print(str1[-1:-4:-1])#方向一致