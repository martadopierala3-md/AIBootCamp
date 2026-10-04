# #string manipulation
# first = "Hello"
# scond = "World"
# #concatenation
# result = first + " " + scond
# #print(result)

# text = "Python programming"
# print(text[0:6])
# print(text[-11])

# name = "Alice"
# age= 25
# print(f"My name is {name} and I am {age} years old.")  #using f-string for formatting string 

#common string methods
#split () - split a string into a list of substrings based on a delimiter default is whitespace

from pydoc import text


sentence = "Python is a fun"
words = sentence.split()
#print(words)  # Output: ['Python', 'is', 'a', 'fun']

#join() - join a list of strings into a single string with a specified delimiter
new_sentence = "|".join(words)
#print(new_sentence)  # Output: "Python|is|a|fun"

#replace() - replace a substring with another substring
text = "I love Java"
text = text.replace("Java", "Python")
#print(text)  # Output: "I love Python"

#strip() - remove leading and trailing whitespace from a string or specified characters from the beginning and end of a string
messy_string = "   Hello, World!   "
cleaned_text = messy_string.strip()
# print(messy_string)  # Output: "   Hello, World!   "
# print(cleaned_text)  # Output: "Hello, World!"

### Regulyar Expressions (Regex) - powerful tool for pattern matching and text manipulation
#search() - search for a pattern in a string and return the first match 

#re Module provides support for regular expressions in Python
import re
#common functions in re module
#re.search() - search for a pattern in a string and return the first match
#re.match() - check if a pattern matches at the beginning of a string
#re.findall() - find all occurrences of a pattern in a string and return them as a list
#re.sub() - replace occurrences of a pattern in a string with a specified replacement

text = "Contact me at = 123-456-7890"
digitsS=re.search(r'[0-9]', text)
print(digitsS)  # Output: <re.Match object; span=(15, 16), match='1'>
digitsF=re.findall(r"\d+", text)
print(digitsF)

updated_text=re.sub(r"\d","X", text)
print(updated_text)



  