import sqlite3
import customtkinter as ctk
from tkinter import messagebox

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("todo.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER DEFAULT 0
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------
task_widgets = {}
selected_task = None  # keep track of selected task

def refresh_list():
    global selected_task
    selected_task = None
    for widget in task_frame.winfo_children():
        widget.destroy()
    task_widgets.clear()

    c.execute("SELECT * FROM tasks")
    for row in c.fetchall():
        task_id, title, done = row

        row_frame = ctk.CTkFrame(task_frame, corner_radius=10)
        row_frame.pack(fill="x", pady=5, padx=5)

        var = ctk.BooleanVar(value=bool(done))
        checkbox = ctk.CTkCheckBox(
            row_frame,
            text=title,
            variable=var,
            command=lambda id=task_id, v=var: toggle_done(id, v)
        )
        checkbox.pack(side="left", padx=10, pady=5)

        del_btn = ctk.CTkButton(
            row_frame,
            text="🗑",
            width=30,
            fg_color="red",
            hover_color="darkred",
            command=lambda id=task_id: delete_task(id)
        )
        del_btn.pack(side="right", padx=5)

        # Make row clickable for selection
        row_frame.bind("<Button-1>", lambda e, id=task_id: select_task(id))
        checkbox.bind("<Button-1>", lambda e, id=task_id: select_task(id))

        task_widgets[task_id] = (row_frame, checkbox, del_btn)

def add_task(event=None):
    title = entry.get()
    if not title.strip():
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    c.execute("INSERT INTO tasks (title, done) VALUES (?, 0)", (title,))
    conn.commit()
    entry.delete(0, "end")
    refresh_list()

def toggle_done(task_id, var):
    c.execute("UPDATE tasks SET done = ? WHERE id = ?", (int(var.get()), task_id))
    conn.commit()

def delete_task(task_id=None):
    global selected_task
    if task_id is None:
        task_id = selected_task
    if not task_id:
        messagebox.showwarning("Warning", "No task selected to delete!")
        return
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    refresh_list()

def select_task(task_id):
    global selected_task
    selected_task = task_id
    # highlight selection
    for tid, (row, _, _) in task_widgets.items():
        row.configure(fg_color=("gray20" if tid == task_id else "transparent"))


def confirm_exit(event=None):
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.destroy()

# ---------------- GUI SETUP ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("📝 Stylish Todo App")
root.geometry("500x500")

title_label = ctk.CTkLabel(root, text="📝 My Todo List", font=("Arial", 22, "bold"))
title_label.pack(pady=15)

input_frame = ctk.CTkFrame(root, corner_radius=10)
input_frame.pack(pady=10, padx=20, fill="x")

entry = ctk.CTkEntry(input_frame, placeholder_text="Enter a new task...")
entry.pack(side="left", expand=True, fill="x", padx=10, pady=10)

add_button = ctk.CTkButton(input_frame, text="Add Task", command=add_task)
add_button.pack(side="right", padx=10, pady=10)

task_frame = ctk.CTkScrollableFrame(root, width=450, height=300, corner_radius=10)
task_frame.pack(pady=10, padx=20, fill="both", expand=True)

refresh_list()

# ---------------- KEY BINDINGS ----------------
root.bind("<Return>", add_task)        # Enter = Add Task
root.bind("<Delete>", lambda e: delete_task())  # Delete key
root.bind("<Escape>", confirm_exit)    # Escape = Exit with confirm

root.mainloop()
