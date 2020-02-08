import pickle

f = open("pickle.pkl","rb")

# 先进先出
print(pickle.load(f))
print(pickle.load(f))
