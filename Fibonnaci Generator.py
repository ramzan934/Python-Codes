print("===== FIBONACCI GENERATOR =====")

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

try:
    n = int(input("How many Fibonacci numbers? "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print(f"First {n} Fibonacci numbers:")
        for num in fibonacci(n):
            print(num, end=" ")

except ValueError:
    print("Invalid input! Enter an integer.")
