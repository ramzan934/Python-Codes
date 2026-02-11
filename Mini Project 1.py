#Mini Project Day 1
# Simple Student Info Program

name = input("Enter student name: ")
marks = float(input("Enter marks: "))

is_pass = marks >= 40

print("\n--- Student Report ---")
print("Name:", name)
print("Marks:", marks)
print("Passed:", is_pass)
print("Data Type of marks:", type(marks))

