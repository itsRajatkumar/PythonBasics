num1=int(input("Enter 1st Number: "))
num2=int(input("Enter 2nd Number: "))
num3=int(input("Enter 3rd Number: "))

if(num1>num2 and num1>num3):
    print(f"{num1} is greatest")

elif(num2>num1 and num2>num3 ):
    print(f"{num2} is greatest")

else:
    print(f"{num3} is greatest")


if(num1<num2 and num1<num3):
    print(f"{num1} is Lowest")

elif(num2<num1 and num2<num3 ):
    print(f"{num2} is Lowest")
    
else:
    print(f"{num3} is Lowest")


    
# print(max(num1,num2,num3)," is Gratest")
# print(min(num1,num2,num3)," is Lowest")

# ans=num1 if num1>num2 and num1>num3 else num2 if num2>num3 else num3
# print(ans," is Gratest")