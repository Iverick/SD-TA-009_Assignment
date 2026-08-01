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
lblTodoItems = Label(text="Add Todo", font=fntLabel, bg=myBgColour, fg=myFgColour)#.pack()
lblTodoItems.grid(column=0, row=1, pady=10)

userInput = Text(height=1, width=20, fg=myFgColour)
userInput.grid(column=0, row=2, padx=10)

# TODO: user input handler
# userInput.bind("<KeyPress>", txtUserInput_KeyPressed)

##########################################################################################
# Setup a following frame that display lists of added and finished Todo
frame = Frame(window)
frame.grid(column=1, row=2, rowspan=4)

# Setup a listbox with label and scrollbar to display added todo activities
lblTodoList = Label(text="Todo Activities", font=fntLabel, bg=myBgColour, fg=myFgColour)
lblTodoList.grid(row=1, column=1)

todoList = Listbox(frame, height=4, fg=myFgColour)
todoList.config(font=("Garmond", 14))
todoList.config(activestyle=NONE)
todoList.pack(side=LEFT)

scrollBar = Scrollbar(frame, orient=VERTICAL)
scrollBar.pack(side=RIGHT, fill=Y)

todoList.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=todoList.yview)

# Setup a listbox with label to display finished todo activities
lblFinishedbox = Label(text="Finished ToDos", font=fntLabel, bg=myBgColour, fg=myFgColour)#.pack()
lblFinishedbox.grid(row=1, column=3)

lstFinishedTodo = Listbox(height=4, fg=myFgColour)
lstFinishedTodo.config(font=("Garmond", 14))
lstFinishedTodo.grid(row=2, column=3, rowspan=4)

##########################################################################################
# Setup framet that holds the buttons container
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
btnMarkFinished = Button(buttonFrame, text="Todo Finished", command=mark_as_finished_clicked)
btnMarkFinished.config(height=buttonHeight, width=buttonWidth, fg=myFgColour)
btnMarkFinished.pack(side='left', padx=buttonPadx)

# Setup unmark todo as finished button
btnUnmarkFinished = Button(buttonFrame, text="Unmark Finished Todo")
btnUnmarkFinished.config(height=buttonHeight, width=buttonWidth, fg=myFgColour)
btnUnmarkFinished.pack(side='left', padx=buttonPadx)

# TODO: load todos to the todo list of page load
load_todos()

# Load the window
window.mainloop()
