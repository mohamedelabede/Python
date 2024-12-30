number =  int(input("Enter Your number : "))
ls = [0,1]
for i in range(2,number+1):
    ls.append(ls[i-1] + ls[i-2])

print(ls)