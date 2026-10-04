# # Reading and writing text files in Python
# #Writing to a file
# with open("notes.txt", "w", encoding="utf-8") as file:
#     file.write("Hello, Python!\n")
#     file.write("This is a text file.")
# #"w" means write. It creates the file or replaces its contents.
# # with closes the file automatically.
# # encoding="utf-8" supports many characters.
# # Reading the entire file
# with open("notes.txt", "r", encoding="utf-8") as file:
#     content = file.read()

# print(content)
# #Reading line by line
# with open("notes.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())
# # Adding text without deleting existing content
# with open("notes.txt", "a", encoding="utf-8") as file:
#     file.write("\nAnother line.")
# #Here, "a" means append.


# #These are Python file modes used with open():
# # Mode	Meaning
# # "r"	Read only. File must already exist.
# # "w"	Write only. Creates a file or replaces existing content.
# # "a"	Append. Adds content to the end; creates the file if needed.
# # "r+"	Read and write. File must already exist; does not automatically erase content.

# open("file.txt", "r")   # read
# open("file.txt", "w")   # write/replace
# open("file.txt", "a")   # add to end
# open("file.txt", "r+")  # read and write

# with open("file.txt", "r", encoding="utf-8") as file:
#     content = file.read()
    
# # Method	What it does
# # read()	Reads the entire file as one string.
# # readline()	Reads one line at a time.
# # readlines()	Reads all lines and returns a list.



# #Methods to write data to a file.
# #write() Writes one string:
# with open("notes.txt", "w") as file:
#     file.write("Hello\n")
#     file.write("Welcome to Python\n")
# #write() does not add a new line automatically, so use \n when needed.

# #writelines()
# #Writes multiple strings from a list or other iterable:
# lines = ["Apple\n", "Banana\n", "Orange\n"]
# with open("fruits.txt", "w") as file:
#     file.writelines(lines)

# #writelines() also does not add new lines automatically:
# #To place each item on a separate line use \n
# file.writelines(["Apple\n", "Banana\n"])

# with open("sample.txt","w") as file:
#     file.write("Hello, World !\n")
#     file.writelines(["Alice\n", "Bob\n", "Cherry\n"])

# with open("sample.txt","r") as file:
#     content = file.read()
#     print(content)

# #just one line     
# with open("sample.txt","r") as file:
#     content = file.readline()
#     print(content)
    
# #list of every line int the file     
# with open("sample.txt","r") as file:
#     content = file.readlines()
#     print(content)
# Advantages of using with for files:
# 1. Closes the file automatically: The file closes automatically when the block ends.
# 2. Safer if an error occurs: Even if an exception happens while reading or writing, Python still closes the file.
# 3. Cleaner code: You do not need to write: file.close()
# 4. Prevents resource leaks: Closing files releases system resources and avoids problems when many files are opened.

# Without with:
# file = open("notes.txt", "r")
# content = file.read()
# file.close()
# With with is generally the recommended approach.

# Exception handling with a try-except block
# A try block contains code that might cause an error.


# try: attempts to run the code. except: handles a specific error.
# The program continues instead of crashing.
# You can also use else and finally:
# try:
#     number = int(input("Enter a number: "))
#     print(10 / number)
# except ValueError:
#     print("Please enter a valid number.")
# except ZeroDivisionError:
#     print("You cannot divide by zero.")

try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError: 
    print("file not found")
    
####PermissionError. It occurs when Python does not have permission to access a file or folder.
try:
    with open("protected.txt", "w") as file:
        file.write("Hello")
except PermissionError:
    print("You do not have permission to write to this file.")


#Common causes: 1. The file is read-only. 2.Another program has locked the file. You lack permission for the folder.
You tried to write to a folder without specifying a filename.
#You can handle it with:
    # except PermissionError as error:
    # print(f"Access denied: {error}")
    
####IOError means an error occurred while performing an input/output operation, such as reading or writing a file.    
try:
    with open("notes.txt", "r", encoding="utf-8") as file:
        content = file.read()
except IOError as error:
    print(f"File operation failed: {error}")
    
#In modern Python, IOError is an alias of OSError.