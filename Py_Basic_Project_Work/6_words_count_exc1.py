#Count Words and lines in the File

def count_words_and_lines(filename):
    try:
        with open(filename,"r") as file:
            lines = file.readlines() # list of iteams 
            line_count =len(lines)
            word_count = sum(len(line.split()) for line in lines) # This counts the total number of words in all lines.
            print(f"Number of lines: {line_count}")
            print(f"Number of words:  {word_count}")
    except FileNotFoundError:
        print(f"File {filename} not found")

count_words_and_lines("sample.txt")
# for line in lines: processes each line.
# line.split(): separates the line into words.
# len(...): counts the words in that line.
# sum(...): adds all line word counts.
# word_count =: stores the total.