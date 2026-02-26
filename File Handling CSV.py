
print("===== FILE HANDLING PRACTICE =====")

# Write to text file
with open("sample.txt", "w") as file:
    file.write("Hello World\n")
    file.write("Python File Handling Example\n")

# Read text file
print("\nReading sample.txt:")
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())

# Append text
with open("sample.txt", "a") as file:
    file.write("Appended line\n")

# CSV Handling
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["John", 22, "New York"])
    writer.writerow(["Alice", 24, "London"])

print("\nReading students.csv:")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

