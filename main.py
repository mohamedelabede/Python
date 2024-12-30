first_number = int(input("First Num : "))
second_number = int(input("Second Num : "))
sum = first_number + second_number
subtraction = first_number - second_number
multiplication =  first_number * second_number
if second_number != 0:
    division = first_number / second_number
else:
    division = "Error: Division by zero"

print("Sum =",sum ,"\n Sub =",subtraction, "\n Multi =",multiplication, "\n Div =",division )