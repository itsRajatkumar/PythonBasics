name="This is testing python. python is best programming language."

search=input("Enter the string you want to search: ")

if(search in name):
    print("yes found at",name.index(search))

else:
    print("Not found")