# -*- coding=utf-8 -*-

def test_dictKey(dict):
    keys=[]
    for key in dict.keys():
        keys.append(key)
    return keys

def test_dictValue(dict):
    values=[]
    for value in dict.values():
        values.append(value)
    return values

def test_dictItems(dict):
    itemValues=[]
    for item in dict.items():
        itemValues.append(item)
    return itemValues

# 拆包
def test_dict(dict):
    for key,value in dict.items():
        print(f'{key}={value}')

if __name__ == '__main__':
    dict1 ={'key1':'abc','key2':'ahhh'}
    print(test_dictKey(dict1))
    print(test_dictValue(dict1))
    print(test_dictItems(dict1))
    test_dict(dict1)