import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete")

def mark_done():
    try:
        selected_task = listbox.curselection()[0]
        task = listbox.get(selected_task)
        listbox.delete(selected_task)
        listbox.insert(tk.END, f"[DONE] {task}")
    except:
        messagebox.showwarning("Warning", "Please select a task")

# GUI setup
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT, padx=(0, 10))

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

del_btn = tk.Button(btn_frame, text="Delete Task", command=delete_task)
del_btn.pack(side=tk.LEFT, padx=5)

done_btn = tk.Button(btn_frame, text="Mark as Done", command=mark_done)
done_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()
