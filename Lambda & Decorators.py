import time

# -------------------------------
# Lambda Functions
# -------------------------------
print("=== Lambda Functions ===")

square = lambda x: x*x
add = lambda a, b: a+b

print("Square of 5:", square(5))
print("Addition 3 + 7:", add(3, 7))

nums = [1, 2, 3, 4, 5]
squares_list = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))

print("Squares List:", squares_list)
print("Even Numbers:", evens)

# -------------------------------
# Decorators
# -------------------------------
print("\n=== Decorators ===")

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f} seconds")
        return result
    return wrapper

@timer
def compute_squares(n):
    return [i**2 for i in range(1, n+1)]

print("Computing squares...")
compute_squares(100000)

