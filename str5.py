# WAF to remove all witespace
def space(s):
    a=''
    for i in s:
        if i!=" ":
            a+=i
    return a
print(space("akash kumar pal"))