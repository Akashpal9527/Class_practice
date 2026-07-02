import json
l=[]
with open("akash.json","r") as f:
    data=json.load(f)
    for i in data:
        l.append(data[i])
print(l)