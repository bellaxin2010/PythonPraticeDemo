import re

f = open("open.txt","r")
data = f.read()
print(re.findall('[0-9]{4,8}',data))
print(re.findall("^a",data))

# 分组
id_num ='310110202001012620'

a = re.search("(?P<province>[0-9]{3})(?P<city>[0-9]{3})(?P<Year>[0-9]{4})",id_num)

print(a.group())
print(a.groups())
print(a.groupdict())

