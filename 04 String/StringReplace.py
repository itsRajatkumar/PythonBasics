name="This is testing python. python is best programmig language."

search=input("Enter the string you want to Replace: ")

word=input("Enter the word you want to Replace with: ")

if(search in name):
    print(f" {search} is Replaced by {word}")
    print("\n--String After Replacement--\n")
    print(name.replace(search,word))

else:
    print("Not found")