import mysql.connector

emp_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="emp_db"
    )

mycur=emp_db.cursor()

sql = "insert into employee_data(emp_id,emp_name,join_date,salary,expirience) valuse (%s,%s,%s,%s,%s)

values = (111,'Riya','2019-02-06','27000','6 Year')

mycur.execute(sql,values)

mydb.commit()

print("Insert Succesfully")
