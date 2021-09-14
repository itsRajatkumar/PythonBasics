i = int(input("Enter a Number: "))

n = i
s = 0

while n > 0:
    digit=n%10
    s=(s*10)+digit
    n //= 10
print(s)

if(s==i):
    print("Palindrom Number")

else:
    print("Not a Palindrom Number")