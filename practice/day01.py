# ==========================
# Variables & Data Types
# ==========================

name = "Abdallah"
age = 24
height = 1.75
is_student = True

print(f"My name is {name}")
print(f"My age is {age}")
print(f"My height is {height}")
print(f"Student: {is_student}")

print("-" * 30)

# ==========================
# Type Casting
# ==========================

number = "100"

print(int(number) + 50)

print("-" * 30)

# ==========================
# Strings
# ==========================

text = "  Python Programming  "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Python", "AI"))
print(text.startswith(" "))
print(text.endswith("g  "))

print("-" * 30)

# ==========================
# Lists
# ==========================

languages = ["Python", "Java", "PHP", "C++"]

print(languages)

languages.append("JavaScript")

print(languages)

languages.remove("PHP")

print(languages)

print(languages[0])
print(languages[-1])

print("-" * 30)

# ==========================
# Tuple
# ==========================

colors = ("Red", "Green", "Blue")

print(colors)

print("-" * 30)

# ==========================
# Set
# ==========================

numbers = {1, 2, 2, 3, 4, 4, 5}

print(numbers)

print("-" * 30)

# ==========================
# Dictionary
# ==========================

student = {"name": "Abdallah", "age": 24, "major": "Computer Science"}

print(student)

student["gpa"] = 94.1

print(student)

student["major"] = "AI Engineering"

print(student)

del student["age"]

print(student)

print("-" * 30)

# ==========================
# Input
# ==========================

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Hello {user_name}")
print(f"Next year you will be {user_age + 1} years old.")
