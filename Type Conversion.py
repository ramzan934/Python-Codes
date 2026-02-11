#Type Conversion
#Convert String to Integer
num_str = "100"
num_int = int(num_str)

print(num_int)
print(type(num_int))

#Convert Integer to Float
num = 50
num_float = float(num)

print(num_float)
print(type(num_float))


#Convert Number to String
age = 25
age_str = str(age)

print(age_str)
print(type(age_str))

#Convert to Boolean
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False
print(bool("Hi"))   # True

#User Input with Type Conversion
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("Name:", name)
print("Age after 5 years:", age + 5)
print("Height:", height)
