import os
import random
import string
def employee(folder):
    curr=os.getcwd()
    path=curr+"\\"+folder
    os.chdir(path)
    file=input("enter your file name:")
    try:
        with open(file,"w") as f:
            id="".join(random.choices(string.ascii_uppercase,k=4))+"".join(random.choices(string.digits,k=4))
            emp_name=input("enter employee name:")
            meeting_id="".join(random.choices(string.ascii_uppercase,k=8))+"".join(random.choices(string.digits,k=8))
            emp_email=input("enter your email id:")
            f.write(f"employee name:{emp_name}")
            f.write(f"\nEmployee ID:{id}")
            f.write(f"\nMeeting ID:https\\ {meeting_id}")
            f.write(f"\nemployee email:{emp_email}")
            print(f"{emp_name} , {id} , {meeting_id} and {emp_email} add successfully!")
    except Exception as e:
        print(e)
folder_name=input("Enter your Folder name:")
try:
    employee(folder_name)
except Exception as e:
    print(e)

    