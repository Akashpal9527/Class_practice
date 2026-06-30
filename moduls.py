# modules: Predefine code wrritten in python for direct usecare without manageing hard code

#  typrs of modules 
# 1. inbuilt modules (random,os,math,string,datetime,faker)
# 2 user-define modules(custome module)

# 1---> Random
import random
mylist=['akash','vivek','arahana','sadhana']

# 1st methods

# res=random.choice(mylist)
# print(res)

# 2nd methods
# weight=[2,3,1,0]
# ak=random.choices(mylist, weights=weight ,k=2)
# print(ak)

# 3rd method
# b=random.randrange(1,10)
# print(b)

# sample()

# res=random.sample(mylist,k=2)
# print(res)

# suffle()
# random.shuffle(mylist)
# print(mylist)


# user max attempt=6
# each attempt random no generate
# fix_value=150

# fix_value=150
# max_attempt=6
# s=0
# # a=random.random()*1000
# l=[]
# while max_attempt>=1:
#     a=int(random.random()*50)
#     l.append(a)
#     s+=a
#     max_attempt-=1
# if s==fix_value:
#     print("equal to the targeted sum is:",s,"all no are",l)
# elif  s<200 and s>100:
#     print("too close and sum is:",s,"all no are",l)
# else:
#     print("too far and sum is:",s,"all no are",l)


# coupon code 
# eg-> CXYZ1234
# d=''
# for i in range(4):
#     a=random.randint(97,122)
#     d+=chr(a).upper()
# for i in range(4):
#     b=random.randint(1,10)
#     d+=str(b)
# print(d)

## 2. DateTime
# import pyautogui
# from datetime import datetime
# import time
# curr_time=datetime.now().strftime("%A/%d-%B/%m/%Y, %H:%M:%S")
# print(curr_time)
# time.sleep(10)
# # pyautogui.typewrite("he")
# for i  in range(100):
#     pyautogui.typewrite("tu bdsk ",interval=0.05)


## # os modules : i will covered in file handling
# math module: self assisment