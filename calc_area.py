import numpy as np
radius = float(input("Enter Radius : "))
circumference = 0
area = 0

circumference = 2 * np.pi * radius
area = np.pi * radius * radius

print("Circumference =",circumference)
print("Area =",area)