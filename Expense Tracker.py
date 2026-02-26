
import json
import os

class ExpenseTracker:
    def __init__(self, file_name="expenses.json"):
        self.file_name = file_name
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                return json.load(f)
        return []

    def save_expenses(self):
        with open(self.file_name, "w") as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, name, amount):
        try:
            amount = float(amount)
            self.expenses.append({"name": name, "amount": amount})
            self.save_expenses()
            print(f"Expense '{name}' of ${amount:.2f} added successfully!")
        except ValueError:
            print("Amount must be a number.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\nAll Expenses:")
        for i, exp in enumerate(self.expenses, start=1):
            print(f"{i}. {exp['name']} - ${exp['amount']:.2f}")

    def delete_expense(self, index):
        try:
            removed = self.expenses.pop(index)
            self.save_expenses()
            print(f"Deleted expense '{removed['name']}' of ${removed['amount']:.2f}")
        except IndexError:
            print("Invalid expense number.")

    def summarize_expenses(self):
        total = sum(exp["amount"] for exp in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Summarize Expenses")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter expense name: ").strip()
            amount = input("Enter amount: ").strip()
            tracker.add_expense(name, amount)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.view_expenses()
            try:
                index = int(input("Enter expense number to delete: ")) - 1
                tracker.delete_expense(index)
            except ValueError:
                print("Enter a valid number.")

        elif choice == "4":
            tracker.summarize_expenses()

        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()

