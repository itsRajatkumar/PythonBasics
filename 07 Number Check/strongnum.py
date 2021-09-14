from math import factorial

num=int(input('Enter a Number: '))

sum=0
temp=num

while(temp>0):
    digit=temp%10
    sum=sum+factorial(digit)
    temp=temp//10

if(num==sum):
    print("Strong Number")

else:
    print("Not a Strong Number")