print("===== CONTEXT MANAGERS =====")

# Using built-in 'with' for files
print("\n--- Built-in context manager ---")
with open("example.txt", "w") as f:
    f.write("Line 1: Using built-in with.\n")
    f.write("Line 2: Automatically closed.")

with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# Custom context manager class
print("\n--- Custom context manager ---")
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return True  # suppress exception

with FileManager("custom_example.txt", "w") as f:
    f.write("Hello! This is custom context manager.\n")
    f.write("File closed automatically.")

with FileManager("custom_example.txt", "r") as f:
    print(f.read())

