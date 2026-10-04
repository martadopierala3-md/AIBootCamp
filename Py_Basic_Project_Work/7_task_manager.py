# Comand Line task Manger 
# Add, view task, mark as complete , delete task

import os

#file to store the task 
FILE_NAME= "task.txt"

#load task from file
def load_tasks():
    tasks = {} # create dictionary with empty task 
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status = line.strip(). split(" | ")
                tasks[int(task_id)]={"title": title, "status":status}
    return tasks

#safe tasks to file
def safe_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")

#add a new task 
def add_task(tasks):
    title = input("Enter task tile")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added")

# view all tasks
def view_task(tasks):
    if not tasks: #empty dictionary
        print("No task avaliable")
    else: 
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task["title"]} - {task['status']}")

#mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete : "))
    if task_id in tasks:
        tasks[task_id]["status"]="complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("Task id not found")

#delete task
def delete_task(tasks):
    task_id = int(input("Enter task ID to Delete : "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted")
    else:
        print("Task id not found")

#Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Menu Menu:")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice= input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
           view_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            safe_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again")
if __name__ == "__main__":
    main()
