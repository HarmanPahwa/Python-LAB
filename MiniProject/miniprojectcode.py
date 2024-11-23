import tkinter as tk
from tkinter import messagebox
import os

# File to store tasks
FILE_NAME = "tasks.txt"

def load_tasks():
    """Load tasks from a file."""
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task, status = line.strip().split(" | ")
                tasks.append({"task": task, "completed": status == "completed"})
    return tasks

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            status = "completed" if task["completed"] else "pending"
            file.write(f"{task['task']} | {status}\n")

def update_task_list():
    """Update the listbox with tasks."""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "[✔]" if task["completed"] else "[✘]"
        task_listbox.insert(tk.END, f"{task['task']} {status}")

def add_task():
    """Add a new task."""
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        task_entry.delete(0, tk.END)
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    """Delete the selected task."""
    try:
        selected_task_index = task_listbox.curselection()[0]
        removed_task = tasks.pop(selected_task_index)
        save_tasks(tasks)
        update_task_list()
        messagebox.showinfo("Task Deleted", f"Task '{removed_task['task']}' deleted!")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_completed():
    """Mark the selected task as completed."""
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index]["completed"] = True
        save_tasks(tasks)
        update_task_list()
        messagebox.showinfo("Task Completed", f"Task '{tasks[selected_task_index]['task']}' marked as completed!")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

def edit_task():
    """Edit the selected task."""
    try:
        selected_task_index = task_listbox.curselection()[0]
        selected_task = tasks[selected_task_index]
        
        # Populate the entry with the selected task's text for editing
        task_entry.delete(0, tk.END)
        task_entry.insert(0, selected_task["task"])
        
        # Remove the selected task from the list temporarily
        tasks.pop(selected_task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

# Load tasks from file
tasks = load_tasks()

# Set up the main window
root = tk.Tk()
root.title("To-Do List")

# Task entry field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5) 

# Task listbox
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

# Mark as completed button
completed_button = tk.Button(root, text="Mark as Completed", width=20, command=mark_completed)
completed_button.pack(pady=5)

# Delete task button
delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

# Edit task button
edit_button = tk.Button(root, text="Edit Task", width=20, command=edit_task)
edit_button.pack(pady=5)

# Update the task list initially
update_task_list()

# Start the Tkinter main loop
root.mainloop()
