import json
with open("product.json",'r') as f:
    a=json.load(f)
    with open("clean.txt","w") as f:
        for i  in a:
            f.write(f"\n{i}:{a.get(i)}")