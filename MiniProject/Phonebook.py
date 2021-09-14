from os import name

import sqlite3

conn=sqlite3.connect('MYPhonebook.db')

print("Phone Book Opened")

while(1):

    print("\n1. Show PhoneBook")
    print("2. Save Number To PhoneBook")
    print("3. Update Number in PhoneBook")
    print("4. Delete Number from PhoneBook")
    print("5. Create PhoneBook")
    print("6. Exit")

    choice=input("Enter Your Choice:")

    if(choice=='1'):
        cursor = conn.execute("SELECT NUMBER, NAME from Phonebook")
        i=1

        for row in cursor:
            print(i,end=". ")
            print(row[1],end=" - ")
            print(row[0])
        print("\nOperation done successfully");

    elif(choice=='2'):
        name=input("Enter Name: ")
        number=input("Enter Contect Number: ")
        conn.execute("INSERT INTO Phonebook (NUMBER, NAME) VALUES(?, ?)",(number, name))
        conn.commit()
        print("Contect inserted successfully");   

    elif(choice=='3'):
        print("What You want to Update\n1. Number\n2. Name")
        ch=input("Enter Choice")

        if(ch==1):
            numold=input("Enter Old Number: ")
            numnew=input("Enter New Number: ")

            try:
                con = sqlite3.connect("MYPhonebook.db")
                cursor = con.cursor()
                print("Updating Contect...")               
                query = "UPDATE Phonebook set NAME =%s where NUMBER =%s"
                val=(numnew,numold)
                conn.execute(query, val)
                conn.commit()
                cursor.close()

            except:
                print("Database Error")

        else:
            numold=input("Enter Number: ")
            namnew=input("Enter New Name: ")

            try:
                conn = sqlite3.connect("MYPhonebook.db")
                cursor = con.cursor()
                print("Updating Contect...")               
                query = "UPDATE Phonebook set NAME =%s where NUMBER =%s"
                val=(numnew,namnew)
                conn.execute(query, val)
                conn.commit()
                cursor.close()

            except:
                print("Database Error")
        print("Contect Updated successfully");

    elif(choice=='4'):
        num=input("Enter Number You Want To Delete: ")

        try:
            conn = sqlite3.connect("MYPhonebook.db")
            cursor = con.cursor()
            print("Deleting Contect...")            
            query = "DELETE from Phonebook where NUMBER = ?"
            cursor.execute(query,(num,))
            conn.commit()
            cursor.close()

        except:
            print("Database Error")
        print("Contect Deleted successfully");

    elif(choice=='5'):
        conn.execute('''CREATE TABLE Phonebook
                (NUMBER INTEGER PRIMARY KEY    NOT NULL,
                NAME           TEXT    NOT NULL);
                ''')
        print("Table created successfully");    

    elif(choice=='6'):
        exit()

    else:
        print("Wrong Input")

conn.close