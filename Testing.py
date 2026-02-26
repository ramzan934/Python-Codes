
import unittest

# -------------------------------
# Calculator Functions
# -------------------------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# -------------------------------
# Unit Tests
# -------------------------------
class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(3, 1), 3)
        with self.assertRaises(ValueError):
            divide(10, 0)

# -------------------------------
# Run Tests & Interactive Calculator
# -------------------------------
if __name__ == "__main__":
    # Run unit tests
    print("===== RUNNING UNIT TESTS =====")
    unittest.main(exit=False)
    
    # Simple CLI calculator
    print("\n===== INTERACTIVE CALCULATOR =====")
    while True:
        print("\nOptions: add, subtract, multiply, divide, exit")
        choice = input("Enter operation: ").strip().lower()
        if choice == "exit":
            print("Exiting calculator...")
            break
        if choice not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid option!")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Enter numeric values.")
            continue

        try:
            if choice == "add":
                print("Result:", add(a, b))
            elif choice == "subtract":
                print("Result:", subtract(a, b))
            elif choice == "multiply":
                print("Result:", multiply(a, b))
            elif choice == "divide":
                print("Result:", divide(a, b))
        except ValueError as ve:
            print("Error:", ve)
