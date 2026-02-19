
print("===== TUPLES PRACTICE =====")

# Create Tuples
numbers = (10, 20, 30, 40, 50)
fruits = ("apple", "banana", "orange")

# Access
print("First number:", numbers[0])
print("Last fruit:", fruits[-1])

# Slicing
print("Slice numbers 1-3:", numbers[1:4])

# Iteration
print("All fruits:")
for fruit in fruits:
    print(fruit)

# Tuple Operations
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print("Concatenated:", t1 + t2)
print("Repeated:", t1 * 2)
print("Length:", len(t1 + t2))
print("Is 2 in t1+t2?", 2 in t1 + t2)


