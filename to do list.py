import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    try:
        selected_task = listbox.curselection()
        listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete")

def clear_tasks():
    listbox.delete(0, tk.END)

# Main window
window = tk.Tk()
window.title("To-Do List")
window.geometry("300x350")
window.configure(bg="light blue")

# Label
title_label = tk.Label(window, text="My To-Do List", font=("Arial", 14), bg="light blue")
title_label.pack(pady=10)

# Entry
task_entry = tk.Entry(window, width=30)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(window, text="Add Task", command=add_task, bg="green", fg="white")
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task, bg="red", fg="white")
delete_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear All", command=clear_tasks, bg="orange")
clear_button.pack(pady=5)

# Listbox
listbox = tk.Listbox(window, width=35, height=10)
listbox.pack(pady=10)

window.mainloop()