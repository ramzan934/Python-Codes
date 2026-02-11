
# String
first_name = "Alice"
last_name = 'Smith'

print(first_name)
print(last_name)

#String Concatenation
full_name = first_name + " " + last_name
print("Full Name:", full_name)

#String Length
print("Length of name:", len(full_name))

#String Indexing
print(full_name[0])   # First character
print(full_name[-1])  # Last character

#String Slicing
print(full_name[0:5])

#String Methods
text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("python", "Java"))
