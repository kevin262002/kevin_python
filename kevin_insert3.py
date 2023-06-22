import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="emp_db"
    )

mycur=mydb.cursor()

sql="insert into employee_data(emp_id,emp_name,salary,expirience)values(%s,%s,%s,%s)"

values=(111,'Riya','26000','6 Year')

mycur.execute(sql,values)

mydb.commit()
