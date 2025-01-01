import numpy as np
def Average(L):
    sum = np.sum(L)
    average = sum / len(L)
    return average

user_input = input("Enter a list of numbers separated by spaces: ")

input_list = list(map(int, user_input.split()))

Av = Average(input_list)
print("Average of list =",Av)