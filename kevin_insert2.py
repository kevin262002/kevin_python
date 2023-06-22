import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="emp_db"
    )

mycur=mydb.cursor()

sql="insert into employee_data(emp_id,emp_name,salary,expirience)values(%s,%s,%s,%s)"

values=(112,'Nency','25000','3 year')

mycur.execute(sql,values)

mydb.commit()
