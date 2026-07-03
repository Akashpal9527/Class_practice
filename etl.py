import json
import pymysql

# function for database connection
def mysql_connect(user,host,password):
    connection=pymysql.connect(user=user,host=host,password=password)
    return connection
mysql=mysql_connect(user="root",host="localhost",password="root")
akash=mysql.cursor()
# print(mysql)

# function for extract the data from json file
def table_json(file):
    with open(f"{file}","r") as f:
        data=json.load(f)
    return data
file="table.json"
data=table_json(file)

# Function to create DataBase
def db_create(db_name):
    try:
        akash.execute(f"create database {db_name}")
        print("DataBase Cresated Successfully!")
        akash.execute(f"show databases")
        print(akash.fetchall())
    except Exception as e:
        print(e)
# database=db_create(data['database'])


# Function To Create Table
def table_create(table_name,database,col_dif):
    try:
        akash.execute(f"use {database}")
        akash.execute(f"create table {table_name} ({col_dif})")
        print("table created successfully!")
    except Exception as e:
        print(e)
col_dif=",".join([f"{col} {dtype}" for col,dtype in data["columns"].items()])
database=data['database']
table=table_create(data['table_name'],database,col_dif)



# Function To insert data into the table
file1="student_profile.json"
student_data=table_json(file1)
def insert_data(table_name,student):
    try:
        akash.execute(f"use {data['database']}")
        akash.execute(f"INSERT INTO {table_name} VALUES ({student})")
        print("Data inserted successfully!")
    except Exception as e:
        print(e)
akash.execute(f"select * from {data['table_name']}")
l=[data[0] for data in akash.fetchall()]
print(l)
for i in range(len(student_data["students"])):
    student = ", ".join(
        f"'{student_data['students'][i][key]}'"
        if isinstance(student_data["students"][i][key], str)
        else str(student_data["students"][i][key])
        for key in student_data["students"][i]
    )
    if int(student[0]) not in l:
        insert_data(data['table_name'],student)
    

mysql.commit()


