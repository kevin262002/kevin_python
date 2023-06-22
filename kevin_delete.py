import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="emp_db"
    )

mycur=mydb.cursor()

sql="delete from employee_data where emp_id=%s"

values=(111,)

mycur.execute(sql,values)

mydb.commit()


