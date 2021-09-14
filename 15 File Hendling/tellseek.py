f = open("Rajat.txt", "r")

f.seek(10)

print(f.tell())
print(f.readline())

f.close()