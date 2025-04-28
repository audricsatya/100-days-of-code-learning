from tkinter import *

# Window 
window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=400, height=600)
window.config(padx=20, pady=10)

# Title Label
# label = Label(text="Miles to Kilometers Converter", font=("Arial", 12, "bold"))
# label.grid(column=1, row=0)
# label.config(pady=20)

# Input Label
miles_label = Label(text="Miles", anchor="w", width=10)
miles_label.grid(column=2, row=1, sticky="w")
kilometers_label = Label(text="Km", anchor="w", width=10)
kilometers_label.grid(column=2, row=2, sticky="w")
is_equal_label = Label(text="is equal to", anchor="e", width=10)
is_equal_label.grid(column=0, row=2, sticky="e")

# Input Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=1)


# Output Label
kilometers_output = Label(text="0")
kilometers_output.grid(column=1, row=2)

# Button Function
def calculate_km():
    miles = float(miles_input.get())
    kilometers = miles * 1.60934
    kilometers_output.config(text=f"{kilometers:.2f}")

button = Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=3)

window.mainloop()

