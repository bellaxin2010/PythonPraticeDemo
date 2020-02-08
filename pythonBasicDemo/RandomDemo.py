import random
import string

t=random.randint(1,10)  # 包括10
print(t)
print(random.randrange(1,10,3)) # 步长
print(random.random()) # 返回浮点数


print(string.ascii_lowercase +string.digits)

sample= string.ascii_lowercase + string.digits
print(random.sample(sample,4)) # 从字符随机选   --- >验证码

#洗牌
a = list(range(100))
print(a)
random.shuffle(a)
print(a)


