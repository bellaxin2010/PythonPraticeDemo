# -*- encoding=utf-8 -*-
#1.请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li＝[‘alex’, ‘eric’, ‘rain’]

li=['alex', 'eric', 'rain']
new_word =li[0]
for i in li[1:]:
    new_word+='_'+i

print(new_word)

#2.查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。
aa = ["  alec", " Aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
#列表
for i,element in enumerate(aa):
    element=element.strip()
    aa[i]=element
    if ((element.startswith('a')or element.startswith('A'))and element.endswith('c')):
        print('以a或A开头并且以c结尾的所有元素:\t'+element)
print(aa)

#元组
for i in tu:
    newTuple=i.strip()
    if((newTuple.startswith('a')or newTuple.startswith('A'))and newTuple.endswith('c')):
        print("查找以a或A开头并且以c结尾的所有元素\t"+newTuple)

#dictionary
for key,value in dic.items():
    newValue=value.strip()
    print("移除空格后："+newValue)
    if ((newValue.startswith('a') or newValue.startswith('A')) and newValue.endswith('c')):
        print("查找以a或A开头并且以c结尾的所有元素\t"+newValue)


#3.写代码，有如下列表，按照要求实现每一个功能

#计算列表长度并输出
li=['alex', 'eric', 'rain']
print(len(li))

#列表中追加元素“seven”，并输出添加后的列表
li.append('senve')
li.insert(len(li),'last')
print(li)
#请删除列表中的元素“eric”，并输出修改后的列表
li.pop(1)
print(li)
#请将列表所有的元素反转，并输出反转后的列表
li.reverse()
print(li)
# #请使用enumrate输出列表元素和序号（序号从100开始）
for i,element in enumerate(li,100):
    print(i,element)

#有如下值集合[11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
dic= [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
upper=[]
lower=[]
for i,element in enumerate(dic):
    if element>66:
        upper.append(element)
    else:
        lower.append(element)
print(upper,lower)

#利用for循环和range输出9 * 9乘法表

for i in range(1,10):
    for j in range(1,10):
        print("{}*{}={}".format(i,j,i*j),end=" ")
    print(" ")




