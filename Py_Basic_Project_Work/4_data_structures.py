#Data structurers : lists, tuples, sets, dictionaries

# numbers = [1, 2, 3, 4, 5]

# fruits = ["apple", "banana", "cherry"]

# mixed = [1, "apple", True]
# # print(numbers[2])
# # print(fruits[-1])
# # print(mixed[0])

# fruits.append("orange")  
# fruits.insert(1, "grape")
# print(fruits)

# fruits.remove("banana")
# print(fruits)

# del fruits[0]
# print(fruits)

# fruits.pop() #removes the last item
# print(fruits)

# sliced_fruits = fruits[1:3]  #slicing 1 before 3
# print(sliced_fruits)

#tuples are immutable
# colors = ("red", "green", "blue")
# single_iteam = ("glass",)        #tuple with one item needs a comma

# print(colors[0])
# print(colors[-1])

#dictionaries are key-value pairs stored for fast lookups
#you can access values by their keys

# student = {"name": "Alice", "age": 25, "grade": "A"}
# print(student)

# print(student["name"])  # Accessing value by key

# student["subject"] = "Math"  # Adding a new key-value pair
# print(student)

# student["age"] = 27  # Updating an existing value
# print(student)

# # del student["grade"]  # Removing a key-value pair
# # print(student)

# # student.pop("subject")  # Removing a key-value pair using pop you need to specify the key
# # print(student)

# #iteration through dictionary using for loop and items() method
# for key, value in student.items():
#     print(f"{key}: {value}")

#sets are unordered collections of unique elements
numbers = {1, 2, 3, 4}

empty_set = set()  # Creating an empty set

print(numbers)
numbers.add(5)  # Adding an element to the set
print(numbers)
numbers.remove(2)  # Removing an element from the set
print(numbers)

#operations on sets union, intersection, difference
# union
set1 = {1, 2, 3}
set2 = {3, 4, 5} 
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
print(set1 | set2)  # Using the | operator for union

# intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}
print(set1 & set2)  # Using the & operator for intersection

# difference
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
print(set1 - set2)  # Using the - operator for difference
