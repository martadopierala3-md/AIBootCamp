#create a text cleaner based in imput form user we will remove punctuation, extra spaces , conver to lower case 
import re

def clean_text(text):
    #remove punpunktuation
    text=re.sub(r"[^\w\s]","",text)
    # \w = word characters: letters, numbers, and _
    # \s = whitespace: spaces, tabs, and newlines
    # ^ inside [] = not
    # Therefore, it matches any character that is not a word character or whitespace—mostly punctuation.
    
    #remove extra spaces
    text = " ".join(text.split())
    text.split() 
    # separates the text wherever there is whitespace and removes extra spaces.
    # " ".join(...) joins the words back together using exactly one space.
    # text = stores the cleaned result back in text.
    
    #convert to lowecase 
    return text.lower()

input_text ="    Hello, World.!!! Welcome to Pyton, Programing ....    "
clean_text = clean_text(input_text)
print(input_text)
print("Clean Text", clean_text)

