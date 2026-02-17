
print("===== LISTS PRACTICE =====")

# Create List
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# Access
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing
print("Slice 1-3:", numbers[1:4])

# Append and Insert
numbers.append(60)
numbers.insert(2, 25)
print("After Append & Insert:", numbers)

# Remove Elements
numbers.remove(25)
popped = numbers.pop()
print("Popped:", popped)
print("List Now:", numbers)

# Sort
numbers.sort()
print("Sorted List:", numbers)

numbers.sort(reverse=True)
print("Descending Sort:", numbers)


