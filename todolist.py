import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "The task cannot be empty.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_task_done():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        task = f"{task} - Done"
        tasks_listbox.insert(tk.END, task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

root = tk.Tk()
root.title("To-Do List Application")

# Frame for Tasks
frame_tasks = tk.Frame(root)
frame_tasks.pack()

# Listbox to display tasks
tasks_listbox = tk.Listbox(frame_tasks, height=10, width=50)
tasks_listbox.pack(side=tk.LEFT)

# Scrollbar for Listbox
scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

tasks_listbox.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=tasks_listbox.yview)

# Task Entry
task_entry = tk.Entry(root, width=50)
task_entry.pack()

# Buttons
add_task_button = tk.Button(root, text="Add Task", width=48, command=add_task)
add_task_button.pack()

mark_done_button = tk.Button(root, text="Mark Task as Done", width=48, command=mark_task_done)
mark_done_button.pack()

delete_task_button = tk.Button(root, text="Delete Task", width=48, command=delete_task)
delete_task_button.pack()

root.mainloop()
