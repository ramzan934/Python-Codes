
print("===== SETS PRACTICE =====")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

# Union
print("Union of A and B:", A.union(B))

# Intersection
print("Intersection of A and B:", A.intersection(B))

# Difference
print("Difference A-B:", A.difference(B))
print("Difference B-A:", B.difference(A))

# Symmetric difference
print("Symmetric Difference:", A.symmetric_difference(B))

# Add & Remove
A.add(7)
print("A after adding 7:", A)

A.remove(1)
print("A after removing 1:", A)

# Loop through set
print("Looping through set B:")
for element in B:
    print(element)

