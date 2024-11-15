# To-Do List Application (Python with Tkinter GUI)

A simple to-do list application built using Python and Tkinter for the graphical user interface (GUI). This app allows users to add, view, delete, and mark tasks as completed. Tasks are stored persistently in a `tasks.txt` file so that they remain available even after closing and reopening the application.

## Features

- **Add Task**: Users can input a new task and add it to the list.
- **View Tasks**: Displays a list of all tasks with their current status (completed or pending).
- **Delete Task**: Removes a selected task from the list.
- **Mark Task as Completed**: Allows users to mark tasks as completed.
- **Persistent Storage**:  Saves tasks to a `tasks.txt` file, so they remain available even after closing the program.

## How It Works

The application uses the Tkinter library for the GUI. Tasks are saved in a `tasks.txt` file with each task having a status (`pending` or `completed`). When you close the application, the tasks are written to the file and reloaded the next time the program starts.

### Example
--- To-Do List ---

1. View tasks
2. Add a task
3. Delete a task
4. Mark task as completed
5. Exit Choose an option (1-5): 1 Your tasks:
 Buy groceries [✘]
 Finish homework [✔] ...

##Interface
###The application window includes:

- An input field to type new tasks.
- A "Add Task" button to add tasks.
- A listbox displaying the current tasks, with the status [✘] for pending tasks and [✔] for completed tasks.
- Buttons to mark a task as completed or delete a task.
