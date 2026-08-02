from tkinter import END, messagebox


unfinished_todos = []
finished_todos = []

DEFAULT_TODOS = ["Buy groceries", "Walk the dog", "Read a book"]

def load_todos(todo_listbox, finished_todo_listbox):
    """
    Method loads list of todos on page load and pushes them into 
    todo_listbox and finished_todo_listbox UI boxes based on their status
    """
    for index, todo in enumerate(DEFAULT_TODOS):
        if index % 2 == 0:
            todo_listbox.insert(END, todo)
        else:
            finished_todo_listbox.insert(END, todo)


def add_todo(todo_input, todo_listbox):
    """
    Method used to generate a new todo entry.
    Grabs user input from todoInput field and pushes into the todoListbox element
    """
    todo = todo_input.get("1.0", END)

    if len(todo.strip()) == 0:
        print("Todo Input field is empty")
        messagebox.showerror("Please enter todo description")

    todo_listbox.insert(END, todo)
    # Cleart input field
    todo_input.delete("1.0", END)


def remove_todo(todo_listbox):
    """
    Method removes selected todo entry
    """
    if todo_listbox.curselection():
        # Return index
        selected_todo = todo_listbox.get(todo_listbox.curselection()[0])
        print(selected_todo)
        todo_listbox.delete(todo_listbox.curselection())
    else:
        print("Please select todo from the list")
        messagebox.showerror("Please select todo from the List")


def mark_todo_finished(todo_list, finished_todo_list):
    """
    Move the selected todo from unfinished to finished
    """
    pass

def unmark_todo_finished(todo_list, finished_todo_list):
    """
    Move the selected todo from finished back to unfinished
    """
    pass
