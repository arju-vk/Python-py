d = {1: 'Alan', 2: 'is', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# # Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():  
    print(f"{key}: {value}")





# del: Removes an item by key.
# pop(): Removes an item by key and returns its value.
# clear(): Empties the dictionary.
# popitem(): Removes and returns the last key-value pair.



d = {1: 'Rahul', 2: 'Ramu', 3: 'Raj', 'age':22}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)



d = { "name": "Prakash", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get(1))