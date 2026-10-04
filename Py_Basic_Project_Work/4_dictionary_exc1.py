#manipulating data in dictionaries
person = {"name": "Alice", "age": 25, "grade": "A"}

#adding a new key-value pair
person["address"] = "123 Main St"

#updating an existing value
person["age"] = 32
print(person)  # Output: {'name': 'Alice', 'age': 32, 'grade': 'A', 'address': '123 Main St'}

#removing a key-value pair
del person["grade"]

print(person)  # Output: {'name': 'Alice', 'age': 32, 'address': '123 Main St'}

