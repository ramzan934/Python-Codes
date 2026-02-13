# ===============================
#        SIMPLE CALCULATOR
# ===============================

print("===== Python Calculator =====")

while True:
    print("\nChoose Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    # Exit Condition
    if choice == "5":
        print("Calculator Closed. Thank You!")
        break

    # Check if valid option selected
    if choice in ["1", "2", "3", "4"]:

        try:
            # Taking numbers from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Performing operation
            if choice == "1":
                result = num1 + num2
                print("Result:", result)

            elif choice == "2":
                result = num1 - num2
                print("Result:", result)

            elif choice == "3":
                result = num1 * num2
                print("Result:", result)

            elif choice == "4":
                if num2 != 0:
                    result = num1 / num2
                    print("Result:", result)
                else:
                    print("Error: Cannot divide by zero")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    else:
        print("Invalid choice! Please select between 1-5.")


