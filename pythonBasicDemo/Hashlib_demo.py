import hashlib

m = hashlib.md5()
m.update("a呵呵".encode("utf-8"))
print(m.digest())
print(m.hexdigest())