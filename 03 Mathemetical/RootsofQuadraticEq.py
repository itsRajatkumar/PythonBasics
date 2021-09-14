import math

a=float(input("Enter the Cofficent of X^2  a: "))

b=float(input("Enter the Cofficent of X  b: "))

c=float(input("Enter the Value of C: "))

root1=(-b + math.sqrt(b**2-4*a*c))/2*a

root2=(-b - math.sqrt(b**2-4*a*c))/2*a

print("Roots are \n x=",root1,"\n x=",root2)