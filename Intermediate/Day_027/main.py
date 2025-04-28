from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=1080, height=720)
window.config(padx=20, pady=20)

# Label
label = Label(text="Hello World", font=("Roboto", 24, "bold"))
label.pack()
label['text'] = "New Text"
# label['bg'] = "blue"
# label['fg'] = "white"
label.config(text="New Text")
# label.place(x=100, y=200)
label.grid(column=0, row=0)

# Button
def button_clicked():
    # print("I got clicked!")
    new_text = entry.get()
    label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=0, row=1)

# Entry
entry = Entry(width=30)
# entry.pack()
entry.grid(column=0, row=2)
entry.get()

window.mainloop()

