while(True):
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))

    print("Enter Your Choice: \n 1: Addition \n 2: Subtraction \n 3:Multiplication \n 4: Division \n 5:Exit")
    c=int(input("Choice: "))

    if c==1:
        print("Addition = ",a+b)
    
    elif c==2:
        print("Subtraction = ",a-b)
    
    elif c==3:
        print("Multiplication = ",a*b)
    
    elif c==4:
        print("Division = ",a/b)
    
    elif c==5:
        print("Exit")
        exit()
    
    else:
        print("please give correct input")


    choice = input("c for continue and q for quit:")
    
    if choice == 'c':
        continue

    elif choice == 'q':
        break

    else :    
        print("please give correct input")