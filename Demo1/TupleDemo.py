# encoding =utf-8
#元组 可以存储多个数据，元组内数据不可更改
# 只有一个数据也要加 ，
# 不支持修改，只支持 查找index , 下标 ，count() ,len()

def tuple_modify(value,index):
    value[index]=7889
    return value

def tuple_change_list(value):
    print(tuple(value))

if __name__ == '__main__':
    listValue=['2dew','cdew']
    tupleValue=('22','212cd',listValue)
    tuple_modify(listValue, 1)
    print(tupleValue)
    print(tupleValue[2][1])
    tuple_change_list(listValue)