from tkinter import *
from eventHandlers import add_clicked, remove_clicked, mark_as_finished_clicked, unmark_as_finished_clicked
from dataHelpers import load_todos

myBgColour = "#9DBDFF"    
myFgColour = "black"
        
# Create a window
window = Tk()
window.minsize(780, 380)
window.title("ToDo App")
window.config(bg=myBgColour)

fntLabel = ("Times New Roman", 14, "italic")

# Adding header label
lblHeading = Label(text="ToDo App", font=("Garamond", 20, "bold"))
lblHeading.config(bg=myBgColour, fg=myFgColour)
lblHeading.grid(row=0, column=0, columnspan=3, pady=10)

# Setting up input text widget
lblTodoItems = Label(text="Add Todo", font=fntLabel, bg=myBgColour, fg=myFgColour)
lblTodoItems.grid(column=0, row=1, pady=10)

todoEntry = Text(height=1, width=20, fg=myFgColour)
todoEntry.grid(column=0, row=2, padx=10)

# TODO: user input handler
# todoEntry.bind("<KeyPress>", txtUserInput_KeyPressed)

##########################################################################################
# Setup a following frame that display lists of added and finished Todo
todoListFrame = Frame(window)
todoListFrame.grid(column=1, row=2, rowspan=4)

# Setup a listbox with label and scrollbar to display added todo activities
lblTodoList = Label(text="Todo Activities", font=fntLabel, bg=myBgColour, fg=myFgColour)
lblTodoList.grid(row=1, column=1)

todoListbox = Listbox(todoListFrame, height=4, fg=myFgColour)
todoListbox.config(font=("Garmond", 14))
todoListbox.config(activestyle=NONE)
todoListbox.pack(side=LEFT)

scrollBar = Scrollbar(todoListFrame, orient=VERTICAL)
scrollBar.pack(side=RIGHT, fill=Y)

todoListbox.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=todoListbox.yview)

# Setup a listbox with label to display finished todo activities
lblFinishedbox = Label(text="Finished ToDos", font=fntLabel, bg=myBgColour, fg=myFgColour)
lblFinishedbox.grid(row=1, column=3)

finishedListbox = Listbox(height=4, fg=myFgColour)
finishedListbox.config(font=("Garmond", 14))
finishedListbox.grid(row=2, column=3, rowspan=4)

##########################################################################################
# Setup frame that holds the buttons container
buttonFrame = Frame(window, bg=myBgColour)
buttonFrame.grid(column=0, row=6, columnspan=4, pady=50)

# Button sizes
buttonHeight = 2
buttonWidth = 20
buttonPadx = 20

# Setup Add Todo button
btnAddTodo = Button(buttonFrame, text="Add Todo", command=add_clicked, fg=myFgColour)
btnAddTodo.config(height=buttonHeight, width=buttonWidth)
btnAddTodo.pack(side='left', padx=buttonPadx)

# Setup Remove Todo button
btnRemoveTodo = Button(buttonFrame, text="Remove Todo", fg=myFgColour)
btnRemoveTodo.config(command=remove_clicked)
btnRemoveTodo.config(height=buttonHeight, width=buttonWidth)
btnRemoveTodo.pack(side='left', padx=buttonPadx)

# Setup mark todo as finished button
btnMarkFinished = Button(buttonFrame, text="Todo Finished",
                         command=lambda: mark_as_finished_clicked(todoListbox, finishedListbox))
btnMarkFinished.config(height=buttonHeight, width=buttonWidth, fg=myFgColour)
btnMarkFinished.pack(side='left', padx=buttonPadx)

# Setup unmark todo as finished button
btnUnmarkFinished = Button(buttonFrame, text="Unmark Finished Todo",
                           command=lambda: unmark_as_finished_clicked(todoListbox, finishedListbox))
btnUnmarkFinished.config(height=buttonHeight, width=buttonWidth, fg=myFgColour)
btnUnmarkFinished.pack(side='left', padx=buttonPadx)

# Load default todos into the arrays and display them
load_todos(todoListbox, finishedListbox)

# Load the window
window.mainloop()
