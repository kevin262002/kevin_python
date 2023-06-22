import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="emp_db"
    )

mycur=mydb.cursor()

sql="delete from emp_data where emp_id=%s"

values=(1005,)

mycur.execute(sql,values)

mydb.commit()

print("succesfull...")
