#Float Input For Height And Base
h = float(input("Entre the height of triangle :"))
b = float(input("Enter the base of trinangle : "))

area = 0.5*h*b
print(f"Area of Triangle is : {area}")

# # using eval function
# # Eval Function Is Used to take multiple value  in row,
# # values are saperated by commas ","
# h,b = eval(input("Enter height and base of triangle using commas : "))
# area = 0.5*h*b
# print(f"Area is : {area}")