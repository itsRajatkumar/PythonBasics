num = int(input("Enter any number :"))

a = 0
if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            a = 1
            break

if a==1:
    print(num, "is not a prime number")

else:
    print(num, "is a prime number")