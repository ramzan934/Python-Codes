
print("===== SAFE DIVISION CALCULATOR =====")

while True:
    try:
        # Taking user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Performing division
        result = num1 / num2

    # If user divides by zero
    except ZeroDivisionError:
        print("Error: You cannot divide by zero! Please try again.\n")

    # If user enters text instead of number
    except ValueError:
        print("Error: Invalid input! Please enter numeric values only.\n")

    # If no error occurs
    else:
        print("Result:", result)
        break   # Exit loop if successful

    # This block always runs
    finally:
        print("Attempt finished.\n")

print("Calculator closed successfully.")

