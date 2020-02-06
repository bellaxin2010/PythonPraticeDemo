# -*——coding=utf8 #
# find() ：查找子串位置 下标，次数
#rfind()

mystr ="hello and,hello and disney!"
#1。find
print(mystr.find('ello'))
print(mystr.find('ello',2,100)) # 开始结束下标
print(mystr.find('2b')) # -1 表示不存在

#2。index 从左侧
print(mystr.index('ell'))
#print(mystr.index('2b'))#不存在报# 错
#3。count 从左侧
print(mystr.count('ell',0,100))

#4。rfind 从右侧
print(mystr.rfind('i'))
print(mystr.find('i'))


## 修改 replace 不修改原有字符串 ，不可变类型数据
print(mystr.replace('ki','ab'))
print(mystr.replace('hello','bell',1)) #1 代表次数

# 2。 split(分割字符， 分割字符个数）
newStr=mystr.split('and',1)
print(newStr)

#3.join  字符或子串。join(多字符串组成的序列）
mylist =['aa2','cbb','cdd']
newStr2=mystr.join(mylist)
print(newStr2)

#4. lower() upper() title()
print(mystr.title())
print(mystr.upper())

#5. 删除首尾字符串 空白字符 Lstrip
newStr3="  abcd    dcd  "
print(newStr3.lstrip())
print(newStr3.rstrip())
print(newStr3.strip()) # 删除两侧

#6。左对齐 ljust  ,字符串序列。ljust(长度，填充字符）
print(mystr.ljust(40,','))
print(mystr.rjust(40,'*'))
print(mystr.center(40,'*')) # 居中对齐

#7。判断真假，true ,false
print(mystr.startswith('and')) # 是否以某个子串开始
print(mystr.endswith('!'))

#8.isalpha() 至少有一个字符
print(mystr.islower())
print(mystr.isalnum()) # 数字或字母或组合
print(mystr.isalpha()) ## 有空格为false， 都是字母包含true
print(mystr.isdigit()) # 数字
print(mystr.isspace()) #空白