from dataHelpers import mark_todo_finished, unmark_todo_finished, add_todo, remove_todo

def add_clicked(todo_entry, todo_listbox):
    add_todo(todo_entry, todo_listbox)

def remove_clicked(todo_listbox):
    remove_todo(todo_listbox)

def mark_as_finished_clicked(todo_listbox, finished_todo_listbox):
    mark_todo_finished(todo_listbox, finished_todo_listbox)

def unmark_as_finished_clicked(todo_list, finished_todo_list):
    unmark_todo_finished(todo_list, finished_todo_list)
