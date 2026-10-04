
#List Comprehension with Conditional. This is a list comprehension with a filter condition. 
# It creates a new list by iterating through items and including only those that meet a condition.
#Syntax: [item for item in iterable if condition]
#How It Works:
#for item in iterable — Loop through each element
#if condition — Filter: only include items where condition is True
#[...] — Creates a list with results

# #create lists of squaers
# #List of ComprConsolidaithing things intiosingle line 
# squares = [x**2 for x in range(10)]
# #print(squares)

# #filter even numbers
# evens = [ x for x in range(20) if x % 2== 0]
# #print(evens)

# #filter odd numbers
# odd = [ x for x in range(20) if x %2 != 0]
# #print(evens)

#lambda functions  How It Works: lambda — Keyword to define an anonymous function
# arguments — Input parameters (can be zero or more)
# expression — Single expression that returns a value
# Returns the result of the expression
#Anonymous single expresion functions defined using lambda keyword

#lambda argument expresion , inline anumaous funcions
# add = lambda x, y : x + y
# print(add(4,5))

###map() applies a function to every item in a list.
numbers = [1, 2, 3, 4]
squares = map(lambda x : x**2, numbers)
print(list(squares))
# def square(n):
#     return n * n
# result = map(square, numbers) #Takes each item from numbers, Calls square(item), Collects the results
# print(list(result)) #[1, 4, 9, 16]

###filter() keeps only items that match a condition.
# numbers = [1, 2, 3, 4, 5, 6]
evenList = filter(lambda x : x % 2 ==0 , numbers)
print(list(evenList))

# def is_even(n):
#     return n % 2 == 0

# result = filter(is_even, numbers) #Checks each item Keeps only those where the function return
# print(list(result)) #[2, 4, 6]

#reduces an iterable into single value reduce is for aggregation
#It turns many values into one value# It is very useful for sums, products, max, min, joining strings, etc.
from functools import reduce

product = reduce(lambda x,y : x * y, numbers)
print(product)