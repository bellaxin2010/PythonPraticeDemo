# dict
# 创建

person = {'key1':'nn','key2':122}
person1= dict(name='key3',age=20,height=100.1)
person3={}.fromkeys([1,2,3,13,4],1000)

#增加

person1['key4']='annce'
### setdefault ,安全方式新增，key有的话就不修改，没有新增
person1.setdefault('name1',1)

# 删除 pop()\ del()
person1.pop('name')
person1.popitem()

#修改
person1['name'] =1113
## update ,2个dict ,有相同key,后面覆盖前面
person1.update(person)

# 查
key=person1.keys()

def getDictKeyValue(dict):
    for key,value in dict.items():
        info = '''------
key :%s 
value:%s
------''' % (key, value)
        print(info)

getDictKeyValue(person1)