name="This is testing python. python is best programmig language."

search=input("Enter the string you want to Count: ")

if(search in name):
    print("Found ",name.count(search),"times")

else:
    print("Not found")