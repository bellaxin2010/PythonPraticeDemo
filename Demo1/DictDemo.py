# coding =utf-8
#字典常见操作：新增 字典序列【key]=value
# 删： del 字典序列【key] , clear()
# 改： 如果存在修改这个Key值，不存在的key新增value ，字典序列【key]=value
# 查找 ：字典序列.get(key,value) ; keys() ; item

def dict_insert(dictValue,value):
    dictValue['key3']=value
    return dictValue

def dict_del(dictValue,key):
    del dictValue[key]
    return dictValue



if __name__ == '__main__':
    list1=['1','32',20]
    tuple1=(2,3)
    dictValue={'key1':list1,'key2':tuple1}
    print(dictValue['key2'])
    print(dict_insert(dictValue,tuple1))
    print(dict_del(dictValue,key='key3'))
    print(dictValue.get('key3')) # 无返回none
    print(dictValue.keys())
    print(dictValue.values())
    print(dictValue.items())