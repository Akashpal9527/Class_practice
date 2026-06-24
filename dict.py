try:
    dic={[2,3,4]:"aka",2:3}
    print(dic)
except TypeError:
    print("list as a key nai ho skata")

# update on dictionary
dk={"aman":"noida","rohan":"delhi",}
# print(dk)
dk["aman"]="Bhadohi"
print(dk)

stu_marks={'aman':300,'shivam':80,'rohan':40,'abhi':44}
s=0
for i in stu_marks:
    s+=stu_marks.get(i)
print(s)

# zip 
l1=['a','b','c','r']
l2=[23,34,67]
res=zip(l1,l2)
print(dict(res))