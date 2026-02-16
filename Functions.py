print("===== FUNCTIONS PRACTICE =====")

# Prime Checker
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Factorial Function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Even/Odd Function
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# User Interaction
num = int(input("Enter a number: "))

print("\nPrime Check:", is_prime(num))
print("Factorial:", factorial(num))
print("Even or Odd:", check_even_odd(num))

