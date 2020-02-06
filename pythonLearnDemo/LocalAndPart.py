name ='al'

def change():
    name = 'abbb'
    age=10
    print(locals())
    print(globals())

change()
print(name)