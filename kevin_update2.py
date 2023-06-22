import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="emp_db"
    )

mycur=mydb.cursor()

sql="update employee_data set emp_name='Dhruvi' where emp_id=%s"

values=(111,)

mycur.execute(sql,values)

mydb.commit()

print("succesfull...")
