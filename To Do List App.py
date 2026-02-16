
print("===== TO-DO LIST APP =====")

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    # Add Task
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View Task
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # Remove Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                print("Removed:", removed)
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Exiting To-Do App. Goodbye!")
        break

    # Invalid
    else:
        print("Invalid choice! Please select 1-4.")


