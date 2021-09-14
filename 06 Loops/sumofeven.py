n=int(input("Enter The Last Range: "))

evensum=0

print("Series of Natural Number:",end=" ")

for i in range(1,n+1):
	print(i,end=" ")

print("\n\nSeries of Even Number:",end=" ")

for i in range(1,n+1):

    if(i % 2 ==0):
        print(i,end=" ")
        evensum=evensum+i

print("\nSum Of Even Number: ",evensum)