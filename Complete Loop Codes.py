
print("===== LOOPS PRACTICE =====")

# 1. For Loop Example
print("\nNumbers 1 to 5 using for loop:")
for i in range(1, 6):
    print(i)

# 2. While Loop Example
print("\nNumbers 1 to 5 using while loop:")
count = 1
while count <= 5:
    print(count)
    count += 1

# 3. Multiplication Table
number = int(input("\nEnter number for table: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# 4. Factorial
num = int(input("\nEnter number for factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial is:", factorial)

# 5. Pattern
print("\nTriangle Pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
