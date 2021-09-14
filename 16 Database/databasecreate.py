import sqlite3

conn=sqlite3.connect('MYDB.db')

print("DataBase Opened")

conn.execute('''CREATE TABLE Employees
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')

print("Table created successfully");