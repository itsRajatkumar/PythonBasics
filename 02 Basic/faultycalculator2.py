num1= int(input("Enter 1st Number: "))

num2= int(input("Enter 2nd Number: "))

num3 = input("Which operation you want  "+"+ , - , / , % , * :")

if num1 == 45 and num2 == 3 and num3 == "*":
    print("555")

elif num1 == 56 and num2 == 9 and num3 == "+":
    print("77")

elif num1 == 56 and num2 == 6 and num3 == "/":
    print("4")

elif num3 == "+":
    sum = num1+num2
    print(sum)

elif num3 == "%":
    rem = num1%num2
    print(rem)

elif num3 == "-":
    sub = num1-num2
    print(sub)

elif num3 == "/":
    div=num1/num2
    print(div)

elif num3 == "*":
    mul=num1*num2
    print(mul)