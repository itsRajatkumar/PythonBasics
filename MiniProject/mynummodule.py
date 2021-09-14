def isperfact(n):
    sum=0

    for i in range(1,n):
        if(n%i==0):
            sum=sum+i

    if(sum==n):
        print("Perfact")

    else:
        print("Not Perfact")


def isarmstrong(num):
    order = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print("Armstrong Number")

    else:
        print("Not a Armstrong Number")


def isstrong(num):
    from math import factorial
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


def ispalindrom(i):
    n = i
    s = 0

    while n > 0:
        digit=n%10
        s=(s*10)+digit
        n //= 10

    if(s==i):
        print("Palindrom Number")

    else:
        print("Not a Palindrom Number")


def ismagic(i):
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