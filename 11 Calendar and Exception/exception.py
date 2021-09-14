try:
    a=int(input("Enter a Char: "))

except Exception as e:
    print("Error: ",e)

try:
    a=[1,2,3]
    print(a[3])

except Exception as e:
    print("Error: ",e)