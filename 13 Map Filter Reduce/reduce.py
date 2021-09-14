from functools import reduce

num=[1,2,3,4,5]

print(reduce((lambda a,b:a+b),num))

print(reduce((lambda a,b:a-b),num))

print(reduce((lambda a,b:a*b),num))

print(reduce((lambda a,b:a/b),num))