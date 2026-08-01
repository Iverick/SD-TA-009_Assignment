from tkinter import END

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
