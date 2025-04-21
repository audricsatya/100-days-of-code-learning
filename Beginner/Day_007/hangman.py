# Hangman Game
# The user has to guess a word by suggesting letters within a certain number of guesses.

import random
import art
from words import word_list

# Choose a random word from the word list
chosen_word = random.choice(word_list)
length_of_chosen_word = len(chosen_word)
end_of_game = False
lives = 6
guess_list = []

# Display the hangman logo and the word to guess
print(art.hangman_logo)

display = []
for letters in chosen_word:
    display.append("_")
print(display)

# Game loop
print("\nWelcome to Hangman!\n")
print("You have 6 lives to guess the word.")
print("The word has", length_of_chosen_word, "letters.\n")
print("You can guess letters one at a time.")
print("If you guess a letter that is not in the word, you will lose a life.")
print("If you guess a letter that is already guessed, you will be prompted to guess again.")
print("\nGood luck!\n")
while not end_of_game:
    guess = input("Guess a letter:").lower()

    if guess not in guess_list:
        guess_list.append(guess)
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = guess

        if guess not in display:
            lives -= 1
            print(art.stages[lives])
            print(f"{guess} is not in the word. You have lost a life.")

        print(display)

        if "_" not in display:
            end_of_game = True
            print("You Win")

        if lives == 0:
            end_of_game = True
            print("You Lose")

    else:
        print(f"You have already guessed {guess}")
        guess_list.append(guess)