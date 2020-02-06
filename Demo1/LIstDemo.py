def listDemo(value):
    # 更新List
    # 增加整个序列到尾
    value.append('3')
    value.append(['1', 1])
    value.insert(1, 'b')
    value.pop(3)
    value.remove('b')
    # value.clear()

    return value


def isReverse(value):
    value.reverse()
    return value

def squareDemo():
    squares = []
    for x in range(19):
        squares.append(x ** 2)
    return squares


def delValue(value, index):
    del value[index]
    return value


def nameIsExist(name):
    if name in listValue:
        print("it exist " + name)
    else:
        print("not exist " + name)


def copyData(value):
    newValue = value.copy()
    return newValue

def valueSort(value):
    i=0
    while i<len(value):
        print(value[i])
        i+=1



if __name__ == '__main__':
    listValue = ['a', '21fe', 'dce']
    print(listDemo(listValue))
    print(listValue)  # 可变
    print(squareDemo())
    nameIsExist('abc')
    print(delValue(listValue, 1))
    print(isReverse(listValue))

    print(copyData(listValue))
    valueSort(listValue)
