import tkinter as tk  # Import Tkinter for creating the graphical user interface (GUI)
from tkinter import messagebox  # Import messagebox for showing pop-up alerts to the user
import os  # Import os for file handling

# File to store tasks
FILE_NAME = "tasks.txt"

def load_tasks():
    """
    Load tasks from a file.
    Reads the file line by line and reconstructs the tasks list with their completion status.
    """
    tasks = []
    if os.path.exists(FILE_NAME):  # Check if the file exists before attempting to read it
        with open(FILE_NAME, "r") as file:
            for line in file:
                task, status = line.strip().split(" | ")  # Split each line into task and status
                tasks.append({"task": task, "completed": status == "completed"})  # Convert "completed" string to boolean
    return tasks

def save_tasks(tasks):
    """
    Save tasks to a file.
    Writes each task with its status ('completed' or 'pending') to the file.
    """
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            status = "completed" if task["completed"] else "pending" 
            file.write(f"{task['task']} | {status}\n")  # Write each task to the file

def update_task_list():
    """
    Update the Listbox widget to display the current tasks.
    Clears the Listbox and repopulates it with tasks and their statuses.
    """
    task_listbox.delete(0, tk.END)  # Clear the current contents of the Listbox
    for task in tasks:
        status = "[✔]" if task["completed"] else "[✘]"  # Display checkmark for completed tasks
        task_listbox.insert(tk.END, f"{task['task']} {status}")  # Add each task to the Listbox

def add_task():
    """
    Add a new task to the task list.
    Reads the user input, adds it to the tasks list, and updates the GUI and file.
    """
    task = task_entry.get()  # Get the task text entered by the user
    if task:  # Ensure the task is not empty
        tasks.append({"task": task, "completed": False})  # Add the new task as pending
        task_entry.delete(0, tk.END)  # Clear the input field
        save_tasks(tasks)  # Save the updated tasks list to the file
        update_task_list()  # update the GUI
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")  # Show warning for empty input

def delete_task():
    """
    Delete the selected task from the task list.
    Updates the file and GUI after deletion.
    """
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the index of the selected task
        removed_task = tasks.pop(selected_task_index)  # Remove the selected task from the list
        save_tasks(tasks)  # Save the updated list to the file
        update_task_list()  # Refresh the GUI
        messagebox.showinfo("Task Deleted", f"Task '{removed_task['task']}' deleted!")  # Notify the user
    except IndexError:  # Handle cases where no task is selected
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_completed():
    """
    Mark the selected task as completed.
    Updates the task's status, file, and GUI.
    """
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the index of the selected task
        tasks[selected_task_index]["completed"] = True  # Update the task status to completed
        save_tasks(tasks)  # Save the updated tasks list to the file
        update_task_list()  # Refresh the GUI
        messagebox.showinfo("Task Completed", f"Task '{tasks[selected_task_index]['task']}' marked as completed!")
    except IndexError:  # Handle cases where no task is selected
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

def edit_task():
    """
    Edit the selected task.
    Populates the input field with the selected task's text for modification.
    """
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the index of the selected task
        selected_task = tasks[selected_task_index]  # Get the selected task
        task_entry.delete(0, tk.END)  # Clear the input field
        task_entry.insert(0, selected_task["task"])  # Insert the task text into the input field
        tasks.pop(selected_task_index)  # Remove the task temporarily from the list
        update_task_list()  # Refresh the GUI
    except IndexError:  # Handle cases where no task is selected
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

# Load tasks from file
tasks = load_tasks()

# Set up the main application window
root = tk.Tk()  # Create the root window
root.title("To-Do List")  # Set the window title

# Task entry field
task_entry = tk.Entry(root, width=40)  # Input field for entering new tasks
task_entry.pack(pady=10)  # Add vertical padding

# Add task button
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)  # Button to add tasks
add_button.pack(pady=5)

# Task Listbox
task_listbox = tk.Listbox(root, width=40, height=10)  # Listbox to display tasks
task_listbox.pack(pady=10)

# Mark as completed button
completed_button = tk.Button(root, text="Mark as Completed", width=20, command=mark_completed)  # Button to mark tasks as completed
completed_button.pack(pady=5)

# Delete task button
delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)  # Button to delete selected tasks
delete_button.pack(pady=5)

# Edit task button
edit_button = tk.Button(root, text="Edit Task", width=20, command=edit_task)  # Button to edit selected tasks
edit_button.pack(pady=5)

# Update the task list on startup
update_task_list()

# Start the Tkinter event loop
root.mainloop()
