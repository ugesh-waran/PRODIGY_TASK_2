import tkinter as tk
from tkinter import simpledialog, messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

def edit_task():
    selected = listbox.curselection()
    if selected:
        current_task = listbox.get(selected)
        new_task = simpledialog.askstring("Edit Task", "Update your task:", initialvalue=current_task)
        if new_task:
            listbox.delete(selected)
            listbox.insert(selected, new_task)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to edit!")

# Setup window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Entry field
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, padx=20, fill="x")

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

edit_btn = tk.Button(btn_frame, text="Edit Task", command=edit_task)
edit_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

# Listbox to display tasks
listbox = tk.Listbox(root, font=("Arial", 14), height=10, selectbackground="lightblue")
listbox.pack(pady=10, padx=20, fill="both", expand=True)

root.mainloop()
