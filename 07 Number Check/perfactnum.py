n=int(input("Enter a Number: "))

sum=0

for i in range(1,n):
    if(n%i==0):
        sum=sum+i

if(sum==n):
    print("Perfact")

else:
    print("Not Perfact")
