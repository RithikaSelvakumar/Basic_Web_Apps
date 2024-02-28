import tkinter as tk
from tkinter import messagebox
import os
import json

def load_tasks(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks, file_name):
    with open(file_name, 'w') as file:
        json.dump(tasks, file)

def add_task():
    task_description = task_entry.get()
    if task_description:
        tasks.append({'description': task_description, 'completed': False})
        save_tasks(tasks, file_name)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task description cannot be empty.")

def list_tasks():
    task_list.delete(0, tk.END)
    for index, task in enumerate(tasks):
        status = 'Done' if task['completed'] else 'Pending'
        task_list.insert(tk.END, f"{index + 1}. [{status}] {task['description']}")

def mark_task_done():
    try:
        selected_index = int(task_list.curselection()[0])
        tasks[selected_index]['completed'] = True
        save_tasks(tasks, file_name)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")
    else:
        list_tasks()

def remove_task():
    try:
        selected_index = int(task_list.curselection()[0])
        del tasks[selected_index]
        save_tasks(tasks, file_name)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")
    else:
        list_tasks()

file_name = 'tasks.json'
tasks = load_tasks(file_name)

root = tk.Tk()
root.title("TODO List")

# Styling
root.configure(bg='#f0f0f0')
root.geometry('400x300')

task_label = tk.Label(root, text="Enter task description:", bg='#f0f0f0', font=('Arial', 12))
task_label.pack()

task_entry = tk.Entry(root, width=50, font=('Arial', 12))
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task, bg='#4caf50', fg='white', font=('Arial', 12))
add_button.pack(pady=5)

list_button = tk.Button(root, text="List Tasks", command=list_tasks, bg='#2196f3', fg='white', font=('Arial', 12))
list_button.pack(pady=5)

task_list = tk.Listbox(root, width=50, height=10, font=('Arial', 12))
task_list.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg='#f44336', fg='white', font=('Arial', 12))
remove_button.pack(pady=5)

mark_done_button = tk.Button(root, text="Mark Task as Done", command=mark_task_done, bg='#ff9800', fg='white', font=('Arial', 12))
mark_done_button.pack(pady=5)

root.mainloop()
