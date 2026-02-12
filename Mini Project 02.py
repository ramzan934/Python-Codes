
# Simple Login Validator

username = "admin"
password = "1234"

input_user = input("Enter username: ")
input_pass = input("Enter password: ")

# Using comparison + logical operators
if input_user == username and input_pass == password:
    print("Login Successful!")
else:
    print("Invalid Credentials!")

# Arithmetic example
num = int(input("Enter a number: "))
print("Square:", num ** 2)

# Membership example
if num in [10, 20, 30]:
    print("Special Number!")


