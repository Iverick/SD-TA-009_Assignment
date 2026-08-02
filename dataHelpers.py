from tkinter import END, messagebox
import mysql.connector

from db_setup import DEFAULT_TODOS, DB_CONFIG

def getConnection():
    """
    Helper function called by the functions used to access the database
    """
    return mysql.connector.connect(**DB_CONFIG)


def load_todos(todo_listbox, finished_todo_listbox):
    """
    Method loads list of todos from the database on page load
    Pushes them into todo_listbox and finished_todo_listbox UI boxes based on their status
    """
    try:
        with getConnection() as conn:
            with conn.cursor() as cursor:

                query = "SELECT body, status FROM todos"
                cursor.execute(query)
                rows = cursor.fetchall()

                for body, status in rows:
                    # Insert each todo entry into listboxes
                    if status == "unfinished":
                        todo_listbox.insert(END, body)
                    else:
                        finished_todo_listbox.insert(END, body)
    except mysql.connector.Error as e:
        print(f"Error connecting: {e}")
        messagebox.showerror("Database Error", "Error selecting todos from the database")


def add_todo(todo_input, todo_listbox):
    """
    Method used to generate a new todo entry.
    Grabs user input from todoInput field and pushes into the todoListbox element
    """
    todo = todo_input.get("1.0", END)

    if len(todo.strip()) == 0:
        print("Todo Input field is empty")
        messagebox.showerror("Error - missing text", "Please enter todo description")

    todo_listbox.insert(END, todo)
    # Cleart input field
    todo_input.delete("1.0", END)


def remove_todo(todo_listbox, finished_todo_listbox):
    """
    Method removes selected todo entry from either of both listbox
    """
    if todo_listbox.curselection():
        # Remove todo from todo_listbox
        print(todo_listbox.get(todo_listbox.curselection()[0]))
        todo_listbox.delete(todo_listbox.curselection())
    elif finished_todo_listbox.curselection():
        # Remove todo from finished_todo_listbox
        print(finished_todo_listbox.get(finished_todo_listbox.curselection()[0]))
        finished_todo_listbox.delete(finished_todo_listbox.curselection())
    else:
        # Display error
        print("Please select todo from the list")
        messagebox.showerror("Error - no selection",
                                        "Please select todo from the List")


def mark_todo_finished(todo_listbox, finished_todo_listbox):
    """
    Move the selected todo from unfinished to finished
    """
    if todo_listbox.curselection():
        # Grab index of the selected todo. Move it to the finished todo listbox and remove from the first listbox
        selected_index = todo_listbox.curselection()
        todo = todo_listbox.get(selected_index[0])
        finished_todo_listbox.insert(END, todo)
        todo_listbox.delete(selected_index)
    else:
        messagebox.showinfo("No selection", 
                                    "Please select an todo from the ToDo activities")


def unmark_todo_finished(todo_list, finished_todo_list):
    """
    Move the selected todo from finished todo listbox back to unfinished todo listbox
    """
    if finished_todo_list.curselection():
        selected_index = finished_todo_list.curselection()
        todo = finished_todo_list.get(selected_index[0])
        todo_list.insert(END, todo)
        finished_todo_list.delete(selected_index)
    else:
        messagebox.showinfo("No selection", 
                                    "Please select an todo from the Finished ToDos")
