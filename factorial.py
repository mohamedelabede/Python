number =  int(input("Enter Your number : "))
result = 1
for i in range(1, number + 1):
    result *= i

print(f'factorial of {number} = {result}')