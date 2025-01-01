def fibonacci(n):
    # Base case: return n for n = 0 or n = 1
    if n <= 1:
        return n
    else:
        # Recursive case: sum of the previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
n = int(input("Enter the number : "))
print(f"Fibonacci of {n} is {fibonacci(n)}")  # Output: Fibonacci of 10 is 55
