# -*- encoding:utf-8 -*-
# g =(x*x for x in range(10))
#
# for i in g:
#     print(i)

# 函数生成器
'''著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, …'''


#
# a = 1 ,a=b
# b =1 ,a+ b
def fib(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        tmp = a
        a = b
        b = tmp + b
        #print(a)
        yield b  # ---> 暂停 ,返回b的值
        count += 1

f=fib(20)
print(next(f))
print(next(f))
print("---- 暂停 yield")
print(next(f))