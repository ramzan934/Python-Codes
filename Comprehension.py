
print("===== COMPREHENSIONS PRACTICE =====")

# List Comprehension
numbers = [i for i in range(1, 6)]
print("Numbers:", numbers)

squares = [i*i for i in range(1, 6)]
print("Squares:", squares)

evens = [i for i in range(1, 11) if i % 2 == 0]
print("Even Numbers:", evens)

# Dictionary Comprehension
square_dict = {i: i*i for i in range(1, 6)}
print("Square Dictionary:", square_dict)

even_square_dict = {i: i*i for i in range(1, 11) if i % 2 == 0}
print("Even Square Dictionary:", even_square_dict)

# Set Comprehension
square_set = {i*i for i in range(1, 6)}
print("Square Set:", square_set)

# Conditional Expression
labels = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]
print("Even/Odd Labels:", labels)

# Nested Comprehension
pairs = [(i, j) for i in range(1, 4) for j in range(1, 4)]
print("Pairs:", pairs)
