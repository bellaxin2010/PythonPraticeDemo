import json

d = {
    "name": "bell",
    "age": 19,
    "blodd": "A"
}

# 打开
with open("json.json","w") as fb:
    json.dump(d,fb)


with open("json.json",) as f:
    #d =json.load(f)
    e =json.load(f)
    #print(d)
    print(e)