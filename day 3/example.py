import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        add_button_to_frame(task)

def add_button_to_frame(task):
    frame = tk.Frame(frame_container, bd=2, relief=tk.GROOVE)
    label = tk.Label(frame, text=task, width=20, anchor='w')
    label.pack(side=tk.LEFT, padx=(5, 0))
    button = tk.Button(frame, text="Delete", command=lambda: delete_task(task))
    button.pack(side=tk.RIGHT, padx=(0, 5))
    frame.pack(fill=tk.X, pady=(2, 0))

def delete_task(task):
    for frame in frame_container.winfo_children():
        label = frame.winfo_children()[0]  # The first widget in the frame is the label
        if label.cget('text') == task:
            frame.destroy()
            break
    listbox.delete(0, tk.END)
    for frame in frame_container.winfo_children():
        listbox.insert(tk.END, frame.winfo_children()[0].cget('text'))

root = tk.Tk()
root.title("To-Do List")

# Entry for adding tasks
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Frame container for list items and buttons
frame_container = tk.Frame(root)
frame_container.pack()

# Listbox to display tasks (optional)
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
listbox.pack(pady=10)

root.mainloop()