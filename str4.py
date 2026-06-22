# WAF to extract only numbers from string
def num(s):
    l=s.split()
    l1=[]
    for i in l:
        a=''
        for j in i:
            if j.isdigit():
                a+=j
        if len(a)!=0:
            l1.append(a)
    return l1
print(num("aks34 kumar23 apl23 jcc jjwwfuyw"))