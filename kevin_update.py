import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="emp_db"
)

mycur=mydb.cursor()

sql = "update employee_data set expirience='2 Year' where emp_id=%s"

values = (108,)

mycur.execute(sql,values)

mydb.commit()

print("Insert Succesfully")
