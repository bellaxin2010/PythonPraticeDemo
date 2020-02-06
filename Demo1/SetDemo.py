# encoding= utf-8

def add_key(value):
    value.add(11)
    return value

if __name__ == '__main__':
    setValue=set([1,',cd','cdw',1])
    print(setValue)
    print(add_key(setValue))