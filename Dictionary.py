print("===== DICTIONARY PRACTICE =====")

# Basic Dictionary
student = {
    "name": "John",
    "age": 21,
    "course": "Python"
}

print("Student Info:", student)

# Access
print("Name:", student["name"])

# Update
student["age"] = 22

# Add
student["grade"] = "A"

# Remove
student.pop("course")

print("Updated Student:", student)

# Loop
print("\nLooping through student:")
for key, value in student.items():
    print(key, ":", value)

# Nested Dictionary
students = {
    "s1": {"name": "John", "age": 21},
    "s2": {"name": "Alice", "age": 22}
}

print("\nNested Dictionary:")
for key, value in students.items():
    print(key, "->", value)

print("Access Nested Value:", students["s1"]["name"])

