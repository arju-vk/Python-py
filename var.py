# All 

# Integer (int) - whole numbers
age = 25
print("Integer:", age, "Type:", type(age))

# Float (float) - decimal numbers
height = 5.9
print("Float:", height, "Type:", type(height))

# String (str) - text
name = "Alice"
print("String:", name, "Type:", type(name))

# Boolean (bool) - True or False
is_student = True
print("Boolean:", is_student, "Type:", type(is_student))

# List (list) - ordered, changeable collection
fruits = ["apple", "banana", "cherry"]
print("List:", fruits, "Type:", type(fruits))

# Tuple (tuple) - ordered, unchangeable collection
coordinates = (10, 20)
print("Tuple:", coordinates, "Type:", type(coordinates))

# Dictionary (dict) - key-value pairs
person = {"name": "Bob", "age": 30}
print("Dictionary:", person, "Type:", type(person))

# Set (set) - unordered, unique elements
unique_numbers = {1, 2, 3, 3}
print("Set:", unique_numbers, "Type:", type(unique_numbers))

# 2. Operators in Python
# Operators perform operations on variables and values.

# Arithmetic Operators
a = 10
b = 3
print("\nArithmetic Operators:")
print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponentiation:", a ** b) # 1000

# Comparison Operators (return True or False)
print("\nComparison Operators:")
print("Equal:", a == b)          # False
print("Not Equal:", a != b)      # True
print("Greater Than:", a > b)    # True
print("Less Than:", a < b)       # False
print("Greater or Equal:", a >= b) # True
print("Less or Equal:", a <= b)  # False

# Logical Operators
x = True
y = False
print("\nLogical Operators:")
print("AND:", x and y)           # False
print("OR:", x or y)             # True
print("NOT:", not x)             # False

# Assignment Operators
c = 5
print("\nAssignment Operators:")
c += 2  # c = c + 2
print("Add and Assign:", c)      # 7
c -= 1  # c = c - 1
print("Subtract and Assign:", c) # 6
c *= 2  # c = c * 2
print("Multiply and Assign:", c) # 12
c /= 3  # c = c / 3
print("Divide and Assign:", c)   # 4.0

# Bitwise Operators (work on binary)
d = 4  # Binary: 100
e = 2  # Binary: 010
print("\nBitwise Operators:")
print("AND:", d & e)             # 0 (Binary: 000)
print("OR:", d | e)              # 6 (Binary: 110)
print("XOR:", d ^ e)             # 6 (Binary: 110)
print("NOT:", ~d)                # -5 (Inverts bits)
print("Left Shift:", d << 1)     # 8 (Binary: 1000)
print("Right Shift:", d >> 1)    # 2 (Binary: 010)

# Membership Operators (check if in sequence)
fruits_list = ["apple", "banana"]
print("\nMembership Operators:")
print("In:", "apple" in fruits_list)      # True
print("Not In:", "grape" not in fruits_list) # True

# Identity Operators (check if same object)
f = [1, 2]
g = [1, 2]
h = f
print("\nIdentity Operators:")
print("Is:", f is h)             # True (same object)
print("Is Not:", f is not g)     # True (different objects, even if equal)

# End of program
print("\nThis covers the basics of Python data types and operators!")
