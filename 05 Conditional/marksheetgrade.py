name=input("Enter Student Name: ")

m1=int(input("Enter 1st Subject Marks: "))
m2=int(input("Enter 2nd Subject Marks: "))
m3=int(input("Enter 3rd Subject Marks: "))
m4=int(input("Enter 4th Subject Marks: "))
m5=int(input("Enter 5th Subject Marks: "))

total=m1+m2+m3+m4+m5
percent=float(total/5)

print("\nStudent Name: ",name)
print("Percentage: ",percent,"%")

if(percent>=90):
    print("Grade A+")

elif(percent>=80 and percent<90):
    print("Grade A")

elif(percent>=70 and percent<80):
    print("Grade B+")

elif(percent>=60 and percent<70):
    print("Grade B")

elif(percent>=50 and percent<60):
    print("Grade C")

elif(percent>=40 and percent<50):
    print("Grade D")

elif(percent>=33 and percent<40):
    print("Grade E")

else:
    print("Fail")