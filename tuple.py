# WAF to extract all no greater than 55

def ext(tup):
    l=[]
    for i in tup:
        if i>=55:
            l.append(i)
    return l
tup=(50,55,69,45,33,78)
res=ext(tup)
print(res)


# Waf to sum of indixesof tuple

def sum_tup(tup):
    s=0
    for i in range(len(tup)):
        s+=i
    return s
tup=(50,55,69,45,33,78)
print(sum_tup(tup))