def Swep(a,b):

    c=a
    a=b
    b=c
    print(f"Values after swaping a = {a}, b = {b}")


X = input("Enter value of a : ")
Y = input("Enter value of b : ")

print(f"Values before swaping a = {X}, b = {Y}")
Swep(X,Y)