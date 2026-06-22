
def rem_word(s):
    l=s.split()
    l1=[]
    for i  in l:
        count=0
        for j in i:
            if j in "aeiou":
                count+=1
        if count==0:
            l1.append(i)
    res=" ".join(l1)
    return res
s="this is python code in vs"
print(rem_word(s))
