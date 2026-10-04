# write and read the list of items
def wirte_item_to_file(filename, items):
    with open(filename,"w") as file:
        for item in items:
            file.write(item + "\n")

def read_item_from_file(filename):
    try:
        with open(filename,"r") as file:
            items = file.readlines()
        print("items in the file: ")
        for item in items:
            print(item.strip()) 
            for item in items: # — Loops through each element in the items collection (list, tuple, string, etc.)
                print(item.strip()) #— For each item:.strip() removes leading and trailing whitespace (spaces, tabs, newlines, etc.)
    except FileNotFoundError: 
        print(f"file {filename} not found") 

fruits =["Apple", "Banana", "Cherry", "Dates"]
wirte_item_to_file("fruits.txt", fruits)
read_item_from_file("fruits.txt")