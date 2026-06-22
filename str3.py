def count_s(s):
    count=0
    for i in s:
        if i ==" ":
            count+=1
    return count
s="this is python code in vs"
print(count_s(s))