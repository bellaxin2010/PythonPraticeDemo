names = ['av', 'cc', 'dd']

str_name = str(names)  # 转字符串
print(str_name)
print(type(str_name))

# eval :  字符串 转换成原有形式
eval_names = eval(str_name)
print(eval_names)
print(type(eval_names))

# filter ,对可迭代对象进行过滤， set(), list() ,dict()


s = list(filter(lambda x: x >= 10, [0, 10, 3, 1, 35, 3, 2, 6, 29]))
print(s)
print(isinstance(s, frozenset))  # 判断 它的数据类型

# map
a ={1,2,3,4}
value=list(map(lambda x:x*2,a))
print(value)

