import pandas as pd

data = pd.read_csv("Intermediate/Day_026/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter your name: ").upper()
alphabet_list = [nato_dict[letter] for letter in name if letter in nato_dict]
print(alphabet_list)