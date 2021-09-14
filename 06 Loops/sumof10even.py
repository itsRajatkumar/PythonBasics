sumeven=0

sumodd=0

for i in range(1,11):

    a=int(input(f"Enter {i} Number: "))

    if(a%2==0):
        sumeven=sumeven+a

    else:
        sumodd=sumodd+a

print("Sum of Even= ",sumeven)
print("Sum of Odd= ",sumodd)