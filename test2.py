import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "Dura1234" )
cursor = mydb.cursor()
#cursor.execute("create database venkat")

#s = "create table venkat.venkatdetails(employeeid int(10) , employeename varchar(30), emailid varchar(30), salary int(10))"
#q1 = cursor.execute(s)

q2 = cursor.execute("select * from venkat.venkatdetails")
print(q2)