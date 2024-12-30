def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(N):
    for num in range(2, N + 1):
        if is_prime(num):
            print(num)

N = int(input("Enter a number N: "))
print(f"Prime numbers between 2 and {N} are:")
print_primes(N)



