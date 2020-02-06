# * coding =utf-8 #

def generator_number(index):
    return (x * x for x in range(index))

def fibon(n):
    a=b=1
    for i in range(n):
        yield a
        a,b=b,a+b

if __name__ == '__main__':
    generator_number(10)
    for i in fibon(100):
        print(i,end= ' ')