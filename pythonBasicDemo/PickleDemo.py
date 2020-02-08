import pickle
'''
dump 写入文件
dumps 生成序列化的字符串

load 从文件加载
loads 把序列化的字符串反向解析
'''

# 序列化
d = {
    "name": "bell",
    "age": 19,
    "blodd": "A"
}

user = ['abb', 18, 'add']

d_dump=pickle.dumps(d)  # bytes

# 反序列化
#print(pickle.loads(d_dump))

# pkl 序列化文件
f=open("pickle.pkl","wb")
pickle.dump(d,f)  # ---> f.write(d)

pickle.dump(user,f)


