import pymysql
import json
import pandas as pd
# function to connect mysql
def db_connection(user,host,password):
    mysql_connection=pymysql.connect(user=user,host=host,password=password)
    return mysql_connection
    
database_connection=db_connection(user="root",host="localhost",password="root")
# print(database_connection)

# Function to create database
def creat_db(db_name):
    conn=database_connection
    akash=conn.cursor()
    try:
        akash.execute(f"create database {db_name}")
        print("DB created successfully!")
        akash.execute("show databases")
        print(akash.fetchall())
    except Exception as e:
        print(e)   
db_name=input("enter your db name:")
creat_db(db_name)
# function To create Table
def create_table(db_name,table_name):
    conn=database_connection
    ravi=conn.cursor()
    try:
        ravi.execute(f"use {db_name}")
        ravi.execute(f"create table {table_name} (id int,title text,description text,category varchar(255),price float,discountPercentage float,rating float,stock int)")
        print("table created successfully!")
        with open("akash.json","r") as f:
            data=json.load(f)
            ravi.execute(f"""INSERT INTO {table_name} VALUES(
                                {data["id"]},
                                '{data["title"]}',
                                '{data["description"]}',
                                '{data["category"]}',
                                {data["price"]},
                                {data["discountPercentage"]},
                                {data["rating"]},
                                {data["stock"]}
                                )""")
            print("data inserted sucessfully!")
            ravi.execute(f"select * from {table_name}")
            res=ravi.fetchall()
            ab=pd.DataFrame(res,columns=['id','title','description','category','price','discountPercentage','rating','stock'])
            print(ab)
    except Exception as e:
        print(e) 
db_name=input("enter your data base name where you wanted to created table:")
table_name=input("enter your table name:")
create_table(db_name,table_name)

