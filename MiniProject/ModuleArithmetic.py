from mymathmodule import *

while(True):

    a=int(input("Enter 1st Number: "))
    b=int(input("Enter 2nd Number: "))

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    print("5. Reminder")

    ch=int(input("Enter Your Choice:"))

    if(ch==1):
        print("Addition=",add(a,b))

    elif(ch==2):
        print("Addition=",sub(a,b))

    elif(ch==3):
        print("Addition=",mul(a,b))

    elif(ch==4):
        print("Addition=",div(a,b))

    elif(ch==5):
        print("Addition=",rem(a,b))

    else:
        print("Worong Input")

    ch=input("Do you want to continue (Y/N): ")

    if(ch=='y' or ch=='Y'):
        continue

    else:
        exit() 