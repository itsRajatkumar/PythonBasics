import math

x = float(input("Enter the Degree : "))

#Sin and Cos are the fuctions of the math module.
sinx = math.sin(x*3.14/180)

cosx = math.cos(x*3.14/180)

print(f"Value of sin {x} = ",sinx)

print(f"Value of cos {x} = ",cosx)