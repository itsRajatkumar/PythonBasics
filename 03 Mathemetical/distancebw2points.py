import math
a,b = eval(input("Enter coordinates of First point Using Commas:- "))
c,d= eval(input("Enter coordinates of Second point Using Commas:- "))
dist=math.sqrt((a-c)**2+((b-d)*(b-d)))
print("Distance is=",dist)