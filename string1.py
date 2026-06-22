# waf to remove last wordin the string
def last_word(s):
    l=s.split()
    l.pop()
    r=" ".join(l)
    return r
res=last_word("akash kumar pal")
print(res)
