#check if string is palindrome
#A palindrome is a word, phrase, or number that reads the same forward and backward.

word = "level"
def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input_text = input("Enter a string ")
if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrone')
else :
    print(f'"{input_text}" is not palindrone')
    
#  word[start:stop:step]   
# start is empty: start automatically
# stop is empty: stop automatically
# step is -1: move backward one character at a time

# if before the string means formatted string (f-string).
# {input_text} is replaced with the variable’s value.
# The single quotes '...' define the Python string.
# The double quotes around {input_text} are printed as visible quotation marks.
# print() displays the result.