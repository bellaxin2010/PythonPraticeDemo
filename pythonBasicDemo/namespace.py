level = 'L0'
n = 22
def func():
    level = 'L1'
    n = 33
    print(locals())
    def outer():
        n = 44
        level = 'L2'
        print("outer:",locals(),n)
        def inner():
            n=55
            level = 'L3'
            print("inner:",locals(),n) #此外打印的n是多少？
        inner()
    outer()
func()