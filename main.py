from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

tasks = []

def add_task():
    task = task_entry.get().strip()
    if task != "":
        tasks.append({"text": task, "completed": False})
        refresh_listbox()
        task_entry.delete(0, END)
        status_label.config(text="🐠 Task added successfully!", fg="#00FFB0")
        window.after(2000, lambda: status_label.config(text=""))
    else:
        status_label.config(text="Please enter a task.", fg="#FF6B6B")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        refresh_listbox()
        status_label.config(text="🦀 Task deleted.", fg="#00FFB0")
        window.after(2000, lambda: status_label.config(text=""))
    except IndexError:
        status_label.config(text="Select a task to delete.", fg="#FF6B6B")

def toggle_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["completed"] = not tasks[selected_index]["completed"]
        refresh_listbox()
        status_label.config(text="🐚 Task updated!", fg="#00FFB0")
        window.after(2000, lambda: status_label.config(text=""))
    except IndexError:
        status_label.config(text="Select a task first.", fg="#FF6B6B")

def clear_all():
    if tasks:
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            tasks.clear()
            refresh_listbox()
            status_label.config(text="All tasks cleared.", fg="#00FFB0")
            window.after(2000, lambda: status_label.config(text=""))
    else:
        status_label.config(text="No tasks to clear.", fg="#FFD166")

def refresh_listbox():
    task_listbox.delete(0, END)
    for task in tasks:
        prefix = "✓ " if task["completed"] else "○ "
        display_text = prefix + task["text"]
        task_listbox.insert(END, display_text)

def on_enter(event):
    add_task()

window = Tk()
window.title("Fish Todo List App")
window.geometry("700x600")
window.resizable(False, False)

bg_image = Image.open("main-background.png").resize((700, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

header_color = "#004E92"
light_blue = "#0D47A1"
semi_light = "#0d1b40"  
entry_bg = "#173D6A"

header_frame = Frame(window, bg=header_color, height=80)
header_frame.pack(fill=X)

title_label = Label(
    header_frame,
    text="🐟 Fish Todo App",
    font=("Segoe UI", 26, "bold"),
    fg="white",
    bg=header_color
)
title_label.pack(pady=8)

subtitle_label = Label(
    header_frame,
    text="Swim through your tasks with ease 🐠",
    font=("Segoe UI", 10),
    fg="#E3F2FD",
    bg=header_color
)
subtitle_label.pack()

content_frame = Frame(window, bg="#001a33") 
content_frame.pack(fill=BOTH, expand=True, padx=20, pady=15)

input_frame = Frame(content_frame, bg="#001a33")
input_frame.pack(fill=X, pady=(0, 15))

task_entry = Entry(
    input_frame,
    font=("Segoe UI", 12),
    width=35,
    bg=entry_bg,
    fg="white",
    relief=FLAT,
    insertbackground="white"
)
task_entry.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))
task_entry.bind("<Return>", on_enter)

add_button = Button(
    input_frame,
    text="+ Fish Add",
    command=add_task,
    width=10,
    bg="#007BFF",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    relief=FLAT,
    cursor="hand2",
    activebackground="#005FCC"
)
add_button.pack(side=LEFT)

buttons_frame = Frame(content_frame, bg="#001a33")
buttons_frame.pack(fill=X, pady=(0, 15))

complete_button = Button(
    buttons_frame,
    text="✓ Fish Complete",
    command=toggle_task,
    width=15,
    bg="#00C853",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief=FLAT,
    cursor="hand2",
    activebackground="#009624"
)
complete_button.pack(side=LEFT, padx=(0, 5))

delete_button = Button(
    buttons_frame,
    text="🗑 Fish Delete",
    command=delete_task,
    width=15,
    bg="#E53935",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief=FLAT,
    cursor="hand2",
    activebackground="#B71C1C"
)
delete_button.pack(side=LEFT, padx=5)

clear_button = Button(
    buttons_frame,
    text="Fish Clear All",
    command=clear_all,
    width=15,
    bg="#FB8C00",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief=FLAT,
    cursor="hand2",
    activebackground="#E65100"
)
clear_button.pack(side=LEFT, padx=5)

listbox_frame = Frame(content_frame, bg="#001a33")
listbox_frame.pack(fill=BOTH, expand=True, pady=(0, 15))

scrollbar = Scrollbar(listbox_frame)
scrollbar.pack(side=RIGHT, fill=Y)

task_listbox = Listbox(
    listbox_frame,
    width=50,
    height=12,
    font=("Segoe UI", 11, "bold"),
    selectmode=SINGLE,
    bg=entry_bg,
    fg="white",
    relief=FLAT,
    bd=0,
    yscrollcommand=scrollbar.set,
    selectbackground="#0066FF"
)
task_listbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=task_listbox.yview)

status_label = Label(
    content_frame,
    text="",
    font=("Segoe UI", 12, "bold"),
    fg="white",
    bg="#001a33"
)
status_label.pack(pady=(5, 0))

window.mainloop()
