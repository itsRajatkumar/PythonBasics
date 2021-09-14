from mynummodule import *

while(True):
    a=int(input("Enter  Number: "))
    

    print("\n1. Perfact Number")
    print("2. Armstrong Number")
    print("3. Strong Number")
    print("4. Palindrom Number")
    print("5. Magic Number")

    ch=int(input("Enter Your Choice:"))
 
    if(ch==1):
        isperfact(a)

    elif(ch==2):
        isarmstrong(a)

    elif(ch==3):
        isstrong(a)

    elif(ch==4):
        ispalindrom(a)

    elif(ch==5):
        ismagic(a)

    else:
        print("Worong Input")

    ch=input("Do you want to continue (Y/N): ")

    if(ch=='y' or ch=='Y'):
        continue

    else:
        exit()
        