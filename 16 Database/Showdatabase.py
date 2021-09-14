import sqlite3

conn=sqlite3.connect('MYDB.db')

print("DATABASE Opened")

cursor = conn.execute("SELECT id, name, address, salary from Employees")

for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully");

conn.close()