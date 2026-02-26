print("===== DAY 17 - MODULES & PACKAGES =====")

# -------------------------------
# Custom Module Usage
# -------------------------------

import my_module

print("\n--- Custom Module ---")
print(my_module.greet("Ali"))
print("Addition:", my_module.add(5, 3))
print("Square:", my_module.square(4))

# -------------------------------
# Math Module
# -------------------------------

import math

print("\n--- Math Module ---")
print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Pi Value:", math.pi)
print("Ceiling:", math.ceil(4.2))
print("Floor:", math.floor(4.8))

# -------------------------------
# Random Module
# -------------------------------

import random

print("\n--- Random Module ---")
print("Random Integer (1-10):", random.randint(1, 10))
print("Random Float:", random.random())

names = ["Ali", "Sara", "John"]
print("Random Choice:", random.choice(names))

random.shuffle(names)
print("Shuffled Names:", names)

# -------------------------------
# Datetime Module
# -------------------------------

import datetime

now = datetime.datetime.now()

print("\n--- Datetime Module ---")
print("Current Date & Time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Time:", now.time())


