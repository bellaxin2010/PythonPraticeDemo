import copy

dic = {'k1': "alex", 'k2': ' aric', "k3": {"a1":"Alex","k4": "Tony"}}

# copy.copy()   浅copy

dic2 = copy.copy(dic)
dic2['k3']['a1']=100
print(dic2)
print(dic)


# copy.deepcopy 深copy
dic3 =copy.deepcopy(dic)
dic3['k3']['a1']=200
print("deepcopy :",dic3)
print("deepcopy :",dic)