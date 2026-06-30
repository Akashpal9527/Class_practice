import os
# print(os.listdir()) #--> list of all files in curent directory

# print(os.getcwd()) #-->current working directory
# print(os.path.exists('aman.txt'))
# try:
#     for i in emp_list:
#         with open(f"{i}.txt","w") as f:
#             f.write(f"hello {i}")
# except Exception as e:
#     print(e)

# for i in emp_list:
#     os.remove(f"{i}.txt")
#     print(f"{i} removed")



 # task
folder="Emp_details"
# os.makedirs(folder)
emp_list=["Aman","shivam","shubham","anshu","kamal"]
curr=os.getcwd()
# print(curr)
path=curr+"\\"+folder
os.chdir(path)
for i in emp_list:
    if not os.path.exists(f"{i}.txt"):
        with open(f"{i}.txt","w") as f:
            f.write(f"hello {i}")
            print(f"{i} created ")
    else:
        print(f"{i} pahale se hi hai ")
