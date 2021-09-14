name=input("Enter Name of Student: ")
roll=input("Enter Roll number: ")

print("Enter marks out of 100-->")
eng = int(input("Marks obtained in english : "))
hin = int(input("Marks obtained in hindi : "))
math = int(input("Marks obtained in math : "))
sci = int(input("Marks obtained in science : "))
his = int(input("Marks obtained in history : "))
percent = ((eng + hin + math + sci + his)/500)*100

print("\n\n")
print("Name of Student- ",name)
print("Roll number- ",roll)
print("Marks Are:")
print(f"\t Hindi- {hin} \n\t English- {eng}\n\t Maths- {math}\n\t Science-{sci}\n\t History-{his} ")
print(f"\nPercentage obtained is = {percent}%")