num=[1,2,3,4,6,5,7,4,6,4]

for i in range(5):
    val=list(map(lambda x:x+5,num))
print(val)

num1=[1,2,3,4,5,6,7,8,9,10]

num2=[1,2,3,4,5,6,7,8,9,10]

for i in range(5):
    val=list(map(lambda x,y:x**y,num1,num2))
print(val)

num=[1,2,3,4,5,6,7,8,9,10]
for i in range(5):
    val=list(map(lambda x:x**2,num))
print(val)

def sq(a):
    return a*a

num=[4,2,9,4,5,7,2,5,1]
for i in range(5):
    val=list(map(sq,num))
print(val)

list1=["RajaT","Kumar","Prajapati"]
ans=list(map(list,list1))
print(ans)