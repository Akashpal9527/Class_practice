import random
l=['rock','paper','scieeor']

user_count=0
com_count=0
for i in range(1,4):
    print("--"*10,f"round {i} start","--"*10)
    user_input=input(""""
        chose 1. for rock,
        chose 2. for paper,
        chose 3. for scieeor:
    """)
    com=random.choice(l)
    print("user choice:",user_input)
    print("computer choice:",com)
    if user_input==com:
        print("your current_score is:",user_count)
        print("computer current_score is:",com_count)
    elif user_input=="rock" and com=='scieeor':
        user_count+=1
        print("your current_score is:",user_count)
        print("computer current_score is:",com_count)
    elif user_input=="rock" and com=='paper':
        com_count+=1
        print("your current_score is:",user_count)
        print("computer current_score is:",com_count)
    elif user_input=="paper" and com=='rock':
        user_count+=1
        print("your current_score is:",user_count)
        print("computer current_score is:",com_count)
    elif user_input=="paper" and com=='scieeor':
        com_count+=1
        print("your current_score is:",user_count)
        print("computer current_score is:",com_count)
    elif user_input=="scieeor" and com=='paper':
        user_count+=1
        print("your current_score is:",user_count)
        print("computer current_score is:",com_count)
    elif user_input=="scieeor" and com=='rock':
        com_count+=1
        print("your current_score is:",user_count)
        print("computer current_score is:",com_count)
    print("--"*10,f"round {i} End","--"*10)
    print()
if user_count==com_count:
    print("match tie")
elif user_count>com_count:
    print("user won")
else:
    print("computer won")
        