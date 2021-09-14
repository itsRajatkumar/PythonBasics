import sqlite3

conn=sqlite3.connect('MYDB.db')
print("DATABASE Opened")

conn.execute("UPDATE Employees set SALARY = 25000.00 where ID = 1")

conn.commit()

print("Total number of rows updated :", conn.total_changes)

print("Operation done successfully");