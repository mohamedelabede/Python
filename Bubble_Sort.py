ls = [3,10,2,7,8,5,1,4,9,6]
n = len(ls)
for i in range(0,n):
    for j in range(0,n-i-1):
        if (ls[j]>ls[j+1]):
            ls[j], ls[j+1] = ls[j+1], ls[j]
            
print(ls)