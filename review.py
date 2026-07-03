review=[
    {
    
     "negative":"This is the very bad product i ordered one months ago",
     "positive":"This product is very nice go for it ",
     "bad_products":["shoes","cricket bat"],
     "good_product":["books","mobiles phone"]

     }
    
]
# print(dic)
# write data into review.txt 


# with open("review.txt","w") as f:
#     for i in dic:
#         if i=="negative" or i=="good_product":
#             f.write(f"\n{i}:{dic[i]}")
    
import pymysql
import pandas as pd
def db_connection(user,host,password):
    mysql_connection=pymysql.connect(user=user,host=host,password=password)
    return mysql_connection
    
database_connection=db_connection(user="root",host="localhost",password="root")
print(database_connection)

akash=database_connection.cursor()
dic=review[0]
db=input("enter database name where you want to create table:")
try:
    akash.execute(f"use {db}")
    table_name=input("enter table name you wanted to create:")
    try:
        l=[]
        for key in dic:
            l.append(key)
        akash.execute(f""" create table {table_name} (
                        {l[0]} varchar(255),
                        {l[1]} varchar(255),
                        {l[2]} varchar(255),
                        {l[3]} varchar(255))
                      """)
        bad = ",".join(dic["bad_products"])
        good = ",".join(dic["good_product"])
        akash.execute(f""" insert into {table_name} values(
                        '{dic["negative"]}',
                        '{dic["positive"]}',
                        '{bad}',
                        '{good}'   
                      )
                      """)
        akash.execute(f"select * from {table_name}")
        res=akash.fetchall()
        ak=pd.DataFrame(res,columns=["negative","positive","bad_products","good_product"])
        print(ak)
    except Exception as e:
        print(e)
except Exception as e:
    print(e)
