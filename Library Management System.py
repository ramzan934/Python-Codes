import json
import os

class Library:
    def __init__(self, file_name="library.json"):
        self.file_name = file_name
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        return []

    def save_books(self):
        with open(self.file_name, "w") as file:
            json.dump(self.books, file)

    def add_book(self, title):
        self.books.append({"title": title, "borrowed": False})
        self.save_books()
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for i, book in enumerate(self.books, start=1):
            status = "Borrowed" if book["borrowed"] else "Available"
            print(f"{i}. {book['title']} - {status}")

    def borrow_book(self, index):
        try:
            book = self.books[index]
            if book["borrowed"]:
                print("Book already borrowed.")
            else:
                book["borrowed"] = True
                self.save_books()
                print("Book borrowed successfully!")
        except IndexError:
            print("Invalid book number.")

    def return_book(self, index):
        try:
            book = self.books[index]
            if not book["borrowed"]:
                print("Book was not borrowed.")
            else:
                book["borrowed"] = False
                self.save_books()
                print("Book returned successfully!")
        except IndexError:
            print("Invalid book number.")


def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            library.add_book(title)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            library.view_books()
            try:
                index = int(input("Enter book number to borrow: ")) - 1
                library.borrow_book(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            library.view_books()
            try:
                index = int(input("Enter book number to return: ")) - 1
                library.return_book(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()


