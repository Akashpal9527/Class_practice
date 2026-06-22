# Waf to print all special symbols
def special(s):
    a=''
    for i in s:
        if i.isalpha() or i.isdigit() or i==" ":
            continue
        else:
            a+=i
    return a
print(special("this is pyth@on prigra12&"))