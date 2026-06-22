#WAF to revers all words from strring
def rev(l):
    l1=[]
    for i in l:
        l1.append(i[::-1])
    return l1
print(rev(["akash" ,"kumar", "pal"]))