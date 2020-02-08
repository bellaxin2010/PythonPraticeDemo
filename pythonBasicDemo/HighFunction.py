#-*- encoding=utf-8 -*-


# str(n).strip("-")    去掉负数
def get_abs(n):
    if n <0:
        return int(str(n).strip("-"))
    return n

def add(x,y,f):
    return f(x)+f(y)


# get_abs 函数名，非函数体传入
print(add(2,-8,get_abs))