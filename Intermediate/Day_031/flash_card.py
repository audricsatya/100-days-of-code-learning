from tkinter import *
import pandas as pd
import random

# ----------------------------------- FLASH CARD APP ----------------------------------- #
# This program is a flash card app that helps users learn a new language by displaying words in the target language
# and their translations. Users can mark words as known or unknown, and the app will keep track of the words to learn.
# The app uses a CSV file to store the words and their translations, and it randomly selects words to display.
# The app also includes a timer that shows the time remaining to learn the words.
# The app is built using the Tkinter library for the user interface and the Pandas library for data manipulation.
# ----------------------------------- FLASH CARD APP ----------------------------------- #
# Constants

BACKGROUND_COLOR = "#B1DDC6"
DELAY = 1000  # 3 seconds delay for showing the English word

# Create the User Interface (UI) with Tkinter

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="Intermediate/Day_031/images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)
canvas.config(highlightthickness=0)

# Words
# Try to read the words from the CSV file, if it doesn't exist, read from the original file
try:
    words = pd.read_csv("Intermediate/Day_031/data/words_to_learn.csv")
    if words.empty:
        words = pd.read_csv("Intermediate/Day_031/data/french_words.csv")
    words_dict = words.to_dict(orient="records")
except FileNotFoundError:
    words = pd.read_csv("Intermediate/Day_031/data/french_words.csv")
    words_dict = words.to_dict(orient="records")

# Get a random word
import random

random_word = random.choice(words_dict)
language = "French"

# Function to show the next word
def next_word(remove_word=False):
    global random_word, word
    if remove_word:
        words_dict.remove(random_word)
    random_word = random.choice(words_dict)
    show_english_word()

# Function to show the English word for 3 seconds before switching to French
def show_english_word():
    global random_word
    english_word = random_word["English"]
    canvas.itemconfig(language_label, text="English")
    canvas.itemconfig(word_label, text=english_word)
    window.after(DELAY, show_french_word)

# Function to show the French word
def show_french_word():
    global random_word
    french_word = random_word["French"]
    canvas.itemconfig(language_label, text="French")
    canvas.itemconfig(word_label, text=french_word)

# Create a label for the language
word = random_word[language]

# Create a label for the word 
language_label = canvas.create_text(400, 150, text=language, font=("Ariel", 40, "italic"), fill="black")

# Create a label for the translation
word_label = canvas.create_text(400, 263, text=word, font=("Ariel", 60, "bold"), fill="black")

# Cross button
cross_img = PhotoImage(file="Intermediate/Day_031/images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=lambda: next_word(remove_word=False))
cross_button.grid(column=0, row=1)

# Check mark button
check_img = PhotoImage(file="Intermediate/Day_031/images/right.png")
check_button = Button(image=check_img, highlightthickness=0, command=lambda: next_word(remove_word=True))
check_button.grid(column=1, row=1)

# Show the first word
show_english_word()

# Save progress to the CSV file
def save_progress():
    words_to_learn = pd.DataFrame(words_dict)
    words_to_learn.to_csv("Intermediate/Day_031/data/words_to_learn.csv", index=False)

# Save progress when the program closes
window.protocol("WM_DELETE_WINDOW", lambda: (save_progress(), window.destroy()))

# Run the program
window.mainloop()