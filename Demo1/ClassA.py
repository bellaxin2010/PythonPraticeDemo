#encoding =utf-8

class ClassA():
    var1 ='ccc'


    def fun1(self):
        print('var1' + self.var1)


def newFun1(self):
    print("vvvd")

a =ClassA();
a.fun1()
print(a.var1)

#改变类属性
ClassA.var1='cdwde'
print(a.var1)

#重写
ClassA.fun1 = newFun1
a.fun1()
