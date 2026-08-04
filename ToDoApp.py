from tkinter import *
from event_handlers import add_clicked, remove_clicked, mark_as_finished_clicked, unmark_as_finished_clicked
from data_helpers import load_todos

def run_app():
    myBgColour = "#9DBDFF"    
    myFgColour = "black"

    # Button colours
    colorAdd = "#4CAF50"
    colorRemove = "#E53935"
    colorToggle = "#3F51B5"
    colorButtonFg = "white"

    placeholderColour = "#3A3A3A"
            
    # Create a window
    window = Tk()
    window.minsize(780, 380)
    window.title("ToDo App")
    window.config(bg=myBgColour)

    fntLabel = ("Times New Roman", 14, "italic")
    fntButton = ("Segoe UI", 11, "bold")
    fntListbox = ("Garamond", 14)

    # Header label
    lblHeading = Label(text="ToDo App", font=("Garamond", 20, "bold"))
    lblHeading.config(bg=myBgColour, fg=myFgColour)
    lblHeading.grid(row=0, column=0, columnspan=3, pady=10)

    # Setting up input text widget
    lblTodoItems = Label(text="Add Todo", font=fntLabel, bg=myBgColour, fg=myFgColour)
    lblTodoItems.grid(column=0, row=1, pady=10)

    todoInput = Text(height=1, width=25, font=fntListbox, fg=placeholderColour)
    todoInput.grid(column=0, row=2, padx=10, sticky="w")

    # TODO: user input handler
    # todoEntry.bind("<KeyPress>", txtUserInput_KeyPressed)

    ##########################################################################################
    # Setup a following frame that display lists of added and finished Todo
    todoListFrame = Frame(window)
    todoListFrame.grid(column=1, row=2, rowspan=4)

    # Setup a listbox with label and scrollbar to display added todo activities
    lblTodoList = Label(text="Todo Activities", font=fntLabel, bg=myBgColour, fg=myFgColour)
    lblTodoList.grid(row=1, column=1)

    todoListbox = Listbox(todoListFrame, height=10, width=25, font=fntListbox, fg=myFgColour)
    todoListbox.config(activestyle=NONE)
    todoListbox.pack(side=LEFT)

    todoScrollBar = Scrollbar(todoListFrame, orient=VERTICAL)
    todoScrollBar.pack(side=RIGHT, fill=Y)

    todoListbox.config(yscrollcommand=todoScrollBar.set)
    todoScrollBar.config(command=todoListbox.yview)

    # Setup a listbox with label and scrollbar to display finished todo activities
    lblFinishedbox = Label(text="Finished ToDos", font=fntLabel, bg=myBgColour, fg=myFgColour)
    lblFinishedbox.grid(row=1, column=3)

    finishedListFrame = Frame(window)
    finishedListFrame.grid(column=3, row=2, rowspan=4)

    finishedListbox = Listbox(finishedListFrame, height=10, width=25, font=fntListbox, fg=myFgColour)
    finishedListbox.config(activestyle=NONE)
    finishedListbox.pack(side=LEFT)

    finishedScrollBar = Scrollbar(finishedListFrame, orient=VERTICAL)
    finishedScrollBar.pack(side=RIGHT, fill=Y)

    finishedListbox.config(yscrollcommand=finishedScrollBar.set)
    finishedScrollBar.config(command=finishedListbox.yview)

    ##########################################################################################
    # Setup frame that holds the buttons container
    buttonFrame = Frame(window, bg=myBgColour)
    buttonFrame.grid(column=0, row=6, columnspan=4, pady=30)

    # Button sizes
    buttonHeight = 2
    buttonWidth = 18
    buttonPadx = 15

    # Setup Add Todo button
    btnAddTodo = Button(buttonFrame, text="Add Todo", font=fntButton, cursor="hand2")
    btnAddTodo.config(command=lambda: add_clicked(todoInput, todoListbox))
    btnAddTodo.config(height=buttonHeight, width=buttonWidth, bg=colorAdd, fg=colorButtonFg, relief=FLAT)
    btnAddTodo.pack(side='left', padx=buttonPadx)

    # Setup Remove Todo button
    btnRemoveTodo = Button(buttonFrame, text="Remove Todo", font=fntButton, cursor="hand2")
    btnRemoveTodo.config(command=lambda: remove_clicked(todoListbox, finishedListbox))
    btnRemoveTodo.config(height=buttonHeight, width=buttonWidth, bg=colorRemove, fg=colorButtonFg, relief=FLAT)
    btnRemoveTodo.pack(side='left', padx=buttonPadx)

    # Setup mark todo as finished button
    btnMarkFinished = Button(buttonFrame, text="Todo Finished", font=fntButton, cursor="hand2")
    btnMarkFinished.config(command=lambda: mark_as_finished_clicked(todoListbox, finishedListbox))
    btnMarkFinished.config(height=buttonHeight, width=buttonWidth, bg=colorToggle, fg=colorButtonFg, relief=FLAT)
    btnMarkFinished.pack(side='left', padx=buttonPadx)

    # Setup unmark todo as finished button
    btnUnmarkFinished = Button(buttonFrame, text="Unmark Finished Todo", font=fntButton, cursor="hand2")
    btnUnmarkFinished.config(command=lambda: unmark_as_finished_clicked(todoListbox, finishedListbox))
    btnUnmarkFinished.config(height=buttonHeight, width=buttonWidth, bg=colorToggle, fg=colorButtonFg, relief=FLAT)
    btnUnmarkFinished.pack(side='left', padx=buttonPadx)

    # Load default todos into the arrays and display them
    load_todos(todoListbox, finishedListbox)

    # Load the window
    window.mainloop()


if __name__ == "__main__":
    run_app()
