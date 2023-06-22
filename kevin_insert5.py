import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="emp_db"
    )

mycur=mydb.cursor()

sql="insert into emp_data(emp_id,emp_name,join_date,salary,experience)values(%s,%s,%s,%s,%s)"

values=(1005,'Niranj Asodariya','2020-12-05','35000','3 Year')

mycur.execute(sql,values)

mydb.commit()

print("succesfull...")
