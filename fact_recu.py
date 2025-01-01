def fact(N):
    #base condition
    if N == 0 or N == 1:
        return 1
    else:
        #return the recursive 
        return N * fact(N-1)
    

Number = int(input("Enter the number : "))
F = fact(Number)
print(f'Factorial {Number} = {F}')