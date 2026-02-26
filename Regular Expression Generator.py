import re

print("===== REGEX VALIDATOR =====")

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r'^(\d{3}-\d{3}-\d{4}|\d{10})$'
    return bool(re.match(pattern, phone))

try:
    email = input("Enter email: ")
    phone = input("Enter phone number: ")

    if validate_email(email):
        print("Valid email!")
    else:
        print("Invalid email!")

    if validate_phone(phone):
        print("Valid phone number!")
    else:
        print("Invalid phone number!")

except Exception as e:
    print("Error:", e)

