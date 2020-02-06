# 交集、包含、 无交集

a ={'key','cc','cd','acce'}
b={'key','cc'}


print(a.isdisjoint(b))  # 判断2个集合是不是不相交，
print(a.issubset(b))  # 判断a是不是b 的子集
print(a.issuperset(b)) #判断a是不是b的父集

print(a.difference(b)) # a-b
print(b.difference(a)) # b -a =set()
print(a.intersection(b))  # a 与b的交集
print(a.union(b)) # 合集
print(a.difference_update(b))  #
print(b.difference_update(a))