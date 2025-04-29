import pandas as pd

data = pd.read_csv("Intermediate/Day_026/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# 1
while True:
    name = input("Enter your name: ").upper()
    if all(letter.isalpha() or letter.isspace() for letter in name):
        alphabet_list = [nato_dict[letter] for letter in name if letter in nato_dict]
        print(alphabet_list)
        break
    else:
        print("Please enter only alphabetic characters.")

# 2
def phonetic_spelling():
    name = input("Enter your name: ").upper()
    try:
        alphabet_list = [nato_dict[letter] for letter in name]
        return alphabet_list
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        return phonetic_spelling()

print(phonetic_spelling())