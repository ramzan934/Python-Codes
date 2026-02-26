print("===== CONTACTS MANAGER =====")

contacts = []

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact added successfully!")

    # View Contacts
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nAll Contacts:")
            for i, contact in enumerate(contacts, start=1):
                print(f"\nContact {i}")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

    # Search Contact
    elif choice == "3":
        search_name = input("Enter name to search: ").lower()
        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name:
                print("\nContact Found:")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True
                break

        if not found:
            print("Contact not found.")

    # Delete Contact
    elif choice == "4":
        delete_name = input("Enter name to delete: ").lower()

        for contact in contacts:
            if contact["name"].lower() == delete_name:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found.")

    # Exit
    elif choice == "5":
        print("Exiting Contacts Manager. Goodbye!")
        break

    # Invalid
    else:
        print("Invalid choice! Please select 1-5.")

