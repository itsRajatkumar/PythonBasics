salary=int(input("Enter Basic Salary: "))

da=salary*.1250
ta=salary*.1350
hra=salary*.1450
pf=salary*.1550
lic=salary*.1650

net= salary + da + ta + hra + pf + lic

print(f"DA={da} \nTA={ta} \nHRA={hra} \nPF={pf} \nLIC={lic} \n")

print("Net Salary=",net)