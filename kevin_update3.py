import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="emp_db"
    )

mycur=mydb.cursor()

sql="update emp_data set salary='90000' where emp_id=%s"

values=(1001,)

mycur.execute(sql,values)

mydb.commit()

print("succesfull...")
