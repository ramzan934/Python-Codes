
print("===== STRING MANIPULATION PRACTICE =====")

text = input("Enter a string: ")

# Slicing
print("First 3 characters:", text[:3])
print("Last 3 characters:", text[-3:])
print("Every second character:", text[::2])

# Reverse
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# Formatting
name = "John"
age = 25
print(f"\nFormatted Example: My name is {name} and I am {age} years old.")

# Palindrome Check
cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("The entered string is a Palindrome.")
else:
    print("The entered string is NOT a Palindrome.")

