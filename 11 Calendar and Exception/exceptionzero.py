a=int(input("Enter a Number: "))

b=int(input("Enter a Number: "))

try:
    c=a/b

except Exception as e:
    print("Error: ",e)

else:
    print("Answer= ",c)