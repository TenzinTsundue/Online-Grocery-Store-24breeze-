from tkinter import *

# Constant
FONT_NAME = "Courier"

# UI Setup

window = Tk()
window.title("24Breeze - Order Compiler")
window.config(padx=50, pady=50, width=200, height=200)

label = Label(text="All uploaded files", font=(FONT_NAME, 15, "bold"), fg= "blue", width=50)
label.grid(row=0, column=0, columnspan=2)

browse_button = Button(text="Browse", width=20, height=5)
browse_button.grid(row=0, column=2)

compile_button = Button(text="Compile", width=20, height=5)
compile_button.grid(row=1, column=2)

show_button = Button(text="Show", width=20, height=5)
show_button.grid(row=2, column=2)

show_label = Label(text='"graps": 2, "banana": 12, "onion": 2, "tomato": 2', font=(FONT_NAME, 8, "bold"), fg= "black", width=50)
show_label.grid(row=1, column=0, columnspan=2, rowspan=3)

send_button = Button(text="Send Mail", width=20, height=5)
send_button.grid(row=3, column=2)





label = Label(text="", font=(FONT_NAME, 15, "bold"), fg= "blue")
label.grid(row="3", column="1")

window.mainloop()