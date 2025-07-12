from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_entry.delete(0, END)
    password_list = []
    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy password to clipboard
    print("Password copied to clipboard.")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not password:
        messagebox.showerror(title="Error", message="Please fill in all fields.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n\nEmail: {email}\nPassword: {password}\n\nIs it ok to save?")
    
    if is_ok:
        with open("intermediate/day_029/password.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            print("Password saved.")
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="intermediate/Day_029/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:", font=("Arial", 10, "bold"), anchor="e")
website_label.grid(column=0, row=1, sticky="e", pady=(0,10))

# Website Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="WE", ipady=5, pady=(0,10))
website_entry.focus()

# Email Label
email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"), anchor="e")
email_label.grid(column=0, row=2, sticky="e", pady=(0,10))

# Email Entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="WE", ipady=5, pady=(0,10))
email_entry.insert(0, "oddey@gmail.com")

# Password Label
password_label = Label(text="Password:", font=("Arial", 10, "bold"), anchor="e")
password_label.grid(column=0, row=3, sticky="e", pady=(0,10))

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="WE", ipady=5, pady=(0,10), padx=(0,10))

# Generate Password Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="we", pady=(0,10), ipady=2 )

# Add Password Button
add_password_button = Button(text="Add", width=36, command=add_password)
add_password_button.grid(column=1, row=4, columnspan=2, sticky="WE", ipady=2)

window.mainloop()