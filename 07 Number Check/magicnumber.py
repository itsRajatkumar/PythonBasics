i=int(input("Enter a Number: "))
a = i
s = 0

while(a>0):
    digit = a%10
    s = s+digit
    a//=10

z = s
s_rev = 0
t= s

while(t>0):
    digit1 = t%10
    s_rev = s_rev*10 + digit1
    t//=10

if(z*s_rev==i):
    print("Magic Number")

else:
    print("Not a Magic Number")