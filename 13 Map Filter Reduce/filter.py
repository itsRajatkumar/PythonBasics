num=(10,9,8,7,4,5,6,3,2,1,5,9,5,7,6,8,5)
print(num)

filteredlist=list(filter(lambda n: n%2==0,num))
print(filteredlist)