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
    and stores it in the database
    """
    todo = todo_input.get("1.0", END)

    if len(todo.strip()) == 0:
        print("Todo Input field is empty")
        messagebox.showerror("Error - missing text", "Please enter todo description")
    else:
        # Add the new entry to the database
        try:
            with getConnection() as conn:
                with conn.cursor() as cursor:
                    insertQuery = 'INSERT INTO todos (body, status) VALUES (%s, %s)'
                    # New todos always start out unfinished
                    cursor.execute(insertQuery, (todo, 'unfinished'))
                    conn.commit()
                    print("Insert was successful")
        except mysql.connector.Error as e:
            print(f"Error inserting into the database, : {e}")
            messagebox.showerror("Database Error", "Error inserting into the database")

        # Update UI and clear input field
        todo_listbox.insert(END, todo)
        todo_input.delete("1.0", END)


def remove_todo(todo_listbox, finished_todo_listbox):
    """
    Method removes selected todo entry from either of both listboxes 
    and corresponding row from the database
    """
    if delete_selected_todo(todo_listbox) or delete_selected_todo(finished_todo_listbox):
        # Delete successful - stop execution
        return

    # Display error
    print("Please select todo from the list")
    messagebox.showerror("Error - no selection",
                                    "Please select todo from the List")


def delete_selected_todo(listbox):
    """
    Helper that removes selected todo from any of listboxes and its
    matching row in the database. Returns True if todo was selected and successfully removed, 
    False if nothing was selected in this listbox.
    """
    if not listbox.curselection():
        return False

    print("Removing todo...")
    selected_index = listbox.curselection()
    todo = listbox.get(selected_index[0])

    # Remove from the database
    try:
        with getConnection() as conn:
            with conn.cursor() as cursor:
                deleteQuery = 'DELETE FROM todos WHERE body = %s LIMIT 1'

                cursor.execute(deleteQuery, (todo,))
                conn.commit()
                print("Delete Successful")

                # Remove todo from the UI
                listbox.delete(selected_index)
    except mysql.connector.Error as e:
        print(f"Error deleting: {e}")
        messagebox.showerror("Database Error", "Error deleting from the database")

    return True
    

def mark_todo_finished(todo_listbox, finished_todo_listbox):
    """
    Move calls update_todo_status helper to change todo status to finished.
    Displays error if the operation was not successful
    """
    if not update_todo_status(todo_listbox, finished_todo_listbox, 'finished'):
        messagebox.showinfo("No selection", 
                                    "Please select an todo from the ToDo activities")


def unmark_todo_finished(todo_listbox, finished_todo_listbox):
    """
    Move calls update_todo_status helper to change todo status to unfinished.
    Displays error if the operation was not successful
    """
    if not update_todo_status(finished_todo_listbox, todo_listbox, 'unfinished'):
        messagebox.showinfo("No selection",
                                    "Please select an todo from the Finished ToDos")


def update_todo_status(source_listbox, target_listbox, new_status):
    """
    Helper that moves the selected item from source_listbox to target_listbox,
    and updates the todo entry status in the database.
    Returns True if anything was selected and updated, False otherwise.
    """
    if not source_listbox.curselection():
        return False
    
    selected_index = source_listbox.curselection()
    todo = source_listbox.get(selected_index[0])

    # Update status in the database
    try:
        with getConnection() as conn:
            with conn.cursor() as cursor:
                update_query = 'UPDATE todos SET status = %s WHERE body = %s LIMIT 1'

                cursor.execute(update_query, (new_status, todo))
                conn.commit()
                print("Update Successful")

                # Move the todo between listboxes
                target_listbox.insert(END, todo)
                source_listbox.delete(selected_index)
    except mysql.connector.Error as e:
        print(f"Error updating: {e}")
        messagebox.showerror("Database Error", "Error updating the database")

    return True
