#word frequency counter
sentence = input("Enter a sentence: ")

words = sentence.split()  #splits the sentence into words
print(words)

#initialize an empty dictionary to store word frequencies
word_count = {}

#count the frequency of each word in the list
for word in words:
    word = word.lower()  #convert to lowercase for case-insensitive counting
    if word in word_count:
        word_count[word] += 1  #increment the count if the word is already in the dictionary
    else:
        word_count[word] = 1  #initialize the count to 1 if the word is not in the dictionary
        
print(word_count)  #print the dictionary with word frequencies
    