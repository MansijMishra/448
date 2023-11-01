import math

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    # Check potential divisors up to the square root of the number
    max_divisor = math.isqrt(number) + 1
    for divisor in range(3, max_divisor, 2):
        if number % divisor == 0:
            return False

    return True

# Test the function with a range of numbers and format the output in two columns
for num in range(3, 101):
    if is_prime(num):
        print(f"{num:2} is prime", end="\t")
    else:
        print(f"{num:2} is not prime", end="\t")
    if (num - 2) % 2 == 0:
        print()  # Start a new row after printing 2 numbers
